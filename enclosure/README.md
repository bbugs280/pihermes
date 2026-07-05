# Enclosure — 3D-Printable STL Files

STL files for the PiHermes enclosure, designed for Beets3D manufacturing (sandstone/SLA).

## Contents (coming soon)

- `pi5-case.stl` — Main enclosure body, fits Raspberry Pi 5
- `usb-dongle-mount.stl` — Mount for USB audio dongle (AB13X or equivalent)
- `ventilation-grill.stl` — Top/bottom vent covers for airflow

## Print Settings (Beets3D)

| Material | Layer Height | Infill | Notes |
|---|---|---|---|
| Sandstone (binder jet) | 0.1mm | N/A | Full color, matte finish |
| SLA Resin | 0.05mm | 100% | Smooth, premium feel |
| PLA (FDM — DIY) | 0.2mm | 20% | For home printers |

## Design Guidelines

- **Acoustic chamber** — the enclosure doubles as a speaker cabinet
- **Heat management** — Pi 5 needs ventilation; leave 5mm clearance
- **Cable routing** — internal channels for USB + power cables
- **LED light pipe** — optional channel for GPIO Neopixel ring

## Status

- [ ] v1 design (functional prototype)
- [ ] v2 design (aesthetic — premium Beets3D finish)
- [ ] Acoustic tuning (bass reflex port sizing)

STL files will be added as Beets3D designs are finalized.
For now, the pipeline works with any USB audio dongle plugged directly into the Pi.
