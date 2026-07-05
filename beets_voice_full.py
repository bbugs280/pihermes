#!/usr/bin/env python3
"""PiHermes voice pipeline — wake word → listen → STT → Hermes → TTS → speak.

This is the production voice pipeline deployed on hermes-pi.
All voice features: openWakeWord, WebRTC VAD, cloud STT (qwen3-asr-flash),
Hermes API, Piper TTS, 5-chime UX, language guard, streaming TTS.

Usage:
  python3 beets_voice_full.py
  # Or as systemd service: sudo systemctl start pihermes-voice
"""

# This file is a placeholder — the actual pipeline lives on hermes-pi at:
# /home/beets3d/beets_voice_full.py
#
# To deploy:
#   cd ~/pihermes
#   bash setup.sh  # copies to ~/.hermes/voice/ and installs systemd service
#
# Source: github.com/bbugs280/pihermes

print("PiHermes voice pipeline — deploy with: bash setup.sh")
print("See: github.com/bbugs280/pihermes")
