"""PiHermes plugin for Hermes Agent — admin tools for the voice pipeline."""

import json
import subprocess
import os

SERVICE_NAME = "pihermes-voice"
PIPELINE_SCRIPT = os.path.expanduser("~/pihermes/beets_voice_full.py")


def _run(cmd: list[str]) -> dict:
    """Run a shell command and return stdout/stderr/exit_code."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return {"ok": r.returncode == 0, "stdout": r.stdout.strip(), "stderr": r.stderr.strip()}
    except subprocess.TimeoutExpired:
        return {"ok": False, "stdout": "", "stderr": "timeout"}
    except Exception as e:
        return {"ok": False, "stdout": "", "stderr": str(e)}


def register(ctx):
    # ── Tool: pihermes_status ──
    def handle_status(params, **kwargs):
        """Check if the voice pipeline is running."""
        del kwargs
        result = _run(["systemctl", "is-active", SERVICE_NAME])
        running = result["ok"] and result["stdout"] == "active"

        # Try to get last log line for activity check
        log_tail = _run(["tail", "-3", "/tmp/voice_v21.log"])
        recent = log_tail.get("stdout", "no log") if log_tail["ok"] else "log unavailable"

        return json.dumps({
            "success": True,
            "pipeline_running": running,
            "service": SERVICE_NAME,
            "recent_log": recent[:300],
        })

    ctx.register_tool(
        name="pihermes_status",
        toolset="pihermes",
        schema={
            "name": "pihermes_status",
            "description": "Check whether the PiHermes voice pipeline is running on this machine.",
            "parameters": {"type": "object", "properties": {}},
        },
        handler=handle_status,
        description="Check whether the PiHermes voice pipeline is running.",
    )

    # ── Tool: pihermes_restart ──
    def handle_restart(params, **kwargs):
        """Restart the voice pipeline service."""
        del kwargs
        result = _run(["systemctl", "restart", SERVICE_NAME])
        return json.dumps({
            "success": result["ok"],
            "message": "Pipeline restarted" if result["ok"] else f"Failed: {result['stderr']}",
        })

    ctx.register_tool(
        name="pihermes_restart",
        toolset="pihermes",
        schema={
            "name": "pihermes_restart",
            "description": "Restart the PiHermes voice pipeline service.",
            "parameters": {"type": "object", "properties": {}},
        },
        handler=handle_restart,
        description="Restart the PiHermes voice pipeline.",
    )

    # ── Hook: log pipeline tool calls ──
    def on_tool_call(tool_name, params, result):
        if tool_name.startswith("pihermes_"):
            print(f"[pihermes] tool called: {tool_name} → {result[:100]}")

    ctx.register_hook("post_tool_call", on_tool_call)
