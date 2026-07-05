#!/usr/bin/env bash
# flash-sd.sh — build a pre-flashed SD card image for PiHermes
#
# Usage: sudo bash flash-sd.sh /dev/diskX
#   (careful! this WILL overwrite the target disk)
#
# Prerequisites:
#   - Raspberry Pi OS Lite (64-bit) image downloaded
#   - Enough disk space for the image (~8GB)
#
# This script:
#   1. Writes Raspberry Pi OS to the SD card
#   2. Mounts the boot partition
#   3. Injects WiFi config + first-boot setup script
#   4. Pre-installs Hermes Agent + PiHermes

echo "PiHermes SD Card Image Builder"
echo "=============================="
echo ""
echo "This is a placeholder script. Full implementation coming in v0.2."
echo ""
echo "Manual steps for now:"
echo "  1. Flash Raspberry Pi OS Lite (64-bit) via Raspberry Pi Imager"
echo "  2. Boot your Pi, SSH in"
echo "  3. curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash"
echo "  4. git clone https://github.com/bbugs280/pihermes && cd pihermes && bash setup.sh"
