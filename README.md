# PiHermes — AI Voice Kit for Raspberry Pi

**"Your Pi. Your AI. Our shell. Plug in and talk."**

PiHermes turns any Raspberry Pi 5 into a voice-controlled AI assistant. It uses [Hermes Agent](https://github.com/NousResearch/hermes-agent) by Nous Research as the brain, with a self-contained voice pipeline (wake word → speech-to-text → AI → text-to-speech) that runs entirely on-device.

## 🎤 What It Does

```
"Hey Bob" → openWakeWord → WebRTC VAD → qwen3-asr-flash (~1s) 
→ Hermes DeepSeek API → Piper TTS → speaker
~10s total cycle from wake to response
```

## 🛒 Kit vs DIY

| | DIY (Free) | Kit ($79) |
|---|---|---|
| Voice pipeline | ✅ Open source | ✅ Pre-installed |
| Enclosure STL | ✅ Download & print | ✅ Premium Beets3D print |
| SD Card | ❌ Flash yourself | ✅ Pre-flashed 32GB |
| USB Mic/Speaker | ❌ Source yourself | ✅ Tested bundle |
| Admin Console | ✅ Hermes plugin | ✅ Pre-configured |

**Kit includes:** 3D-printed enclosure + pre-flashed SD card + USB mic/speaker + setup script. You bring your own Pi 5.

## ⚡ Quick Install (DIY)

```bash
git clone https://github.com/bbugs280/pihermes
cd pihermes
bash setup.sh
```

This installs:
- Voice pipeline (`beets_voice_full.py`) + systemd service
- Hermes dashboard plugin (admin console)
- openWakeWord + custom "Hey Bob" wake word
- Piper TTS + voice models
- WebRTC VAD for smart silence detection

## 📦 What's Inside

```
pihermes/
├── beets_voice_full.py        ← Voice pipeline (wake → STT → Hermes → TTS)
├── setup.sh                    ← One-command installer
├── hermes-plugin/              ← Hermes Agent plugin
│   ├── plugin.yaml
│   ├── __init__.py             ← Tools: status, config, restart
│   ├── dashboard/
│   │   ├── manifest.json
│   │   ├── dist/index.js       ← Admin console tab
│   │   └── dist/style.css
│   └── plugin_api.py           ← FastAPI backend routes
├── enclosure/                  ← 3D-printable STL files
│   └── README.md               ← Print settings, materials
├── docs/
│   └── quickstart.md
└── scripts/
    └── flash-sd.sh              ← SD card image builder
```

## 🔧 Requirements

- Raspberry Pi 5 (or Pi 4 with USB audio dongle)
- USB microphone + speaker (or combo dongle)
- Hermes Agent installed
- DeepSeek API key (or any Hermes-supported provider)
- Python 3.10+

## 🏗️ Architecture

```
USB Audio Dongle          Raspberry Pi 5
┌──────────────┐         ┌──────────────────────────┐
│ arecord (mic)│  PCM    │ openWakeWord (onnx)      │
│      ↕       │←───────→│  → "Hey Bob" detection   │
│ aplay (spkr) │         │       ↓                  │
└──────────────┘         │ WebRTC VAD (silence)     │
                         │       ↓                  │
                         │ qwen3-asr-flash (cloud)  │
                         │       ↓                  │
                         │ Hermes API (localhost)    │
                         │       ↓                  │
                         │ Piper TTS → speaker      │
                         └──────────────────────────┘
```

## 🌐 Community

- **Hermes Agent:** [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **PiHermes discussions:** [GitHub Discussions](https://github.com/bbugs280/pihermes/discussions)

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE)
