# Conduction Mechanism Analysis

A modular Python toolkit for segmenting I-V data and classifying conduction mechanisms (Ohmic, SCLC, Schottky, Poole-Frenkel, FN tunneling, etc.) in resistive devices.

## Structure

- `mechanisms/` — Individual mechanism detection modules
- `segmentation/` — Log-log segmentation code
- `utils/` — I/O, plotting, and fitting helpers
- `classify.py` — Classifies mechanism for each segment
- `main.py` — Main runner and demo
- `data/` — Place your CSV files here

## Usage

```bash
python main.py
```

Edit `main.py` for your data location and classification/segmentation parameters.
