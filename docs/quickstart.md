# PiHermes — Quick Start Guide

## Prerequisites

- Raspberry Pi 5 (or Pi 4)
- USB microphone + speaker (or combo audio dongle)
- Hermes Agent installed
- DeepSeek API key (or any Hermes-compatible provider)
- Python 3.10+

## Install (3 commands)

```bash
# 1. Clone the repo
git clone https://github.com/bbugs280/pihermes
cd pihermes

# 2. Run the installer
bash setup.sh

# 3. Start the voice pipeline
systemctl --user enable --now pihermes-voice
```

## Verify

1. Open Hermes dashboard: `http://<pi-ip>:9119`
2. Click the **PiHermes** tab — you should see "Running" status
3. Say **"Hey Bob"** near the Pi — it should beep and respond

## Troubleshooting

```bash
# Check pipeline status
systemctl --user status pihermes-voice

# View logs
journalctl --user -u pihermes-voice -f

# Restart
systemctl --user restart pihermes-voice

# Test mic/speaker
arecord -D plughw:2,0 -d 2 test.wav
aplay -D plughw:2,0 test.wav
```

## Architecture

```
USB Audio → openWakeWord → WebRTC VAD → qwen3-asr-flash (cloud)
→ Hermes API (localhost:8642) → Piper TTS → USB Speaker
```

## Next Steps

- [Configure wake word](docs/wake-word.md) (coming soon)
- [Change voice](docs/voice.md) (coming soon)
- [Admin console](http://localhost:9119/pihermes)
