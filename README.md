# Extreme-Aware Hybrid Emulators of Dynamic Global Vegetation Models with Latent Active Root-Zone Storage for Low-Latency Carbon Monitoring

## Overview
Hybrid convolutional emulators of TRENDY DGVMs that jointly predict monthly gridded NBP and diagnose a latent active root-zone storage (aS_rz) state. Explicitly improves skill on climate extremes and disturbance events through weighted losses and auxiliary fire/drought inputs.

Reduces recursive error accumulation, raises grid-scale anomaly skill during droughts, heatwaves and fires, and enables near-real-time diagnostic carbon budgets.

## Objective
Develop hybrid convolutional emulators of TRENDY DGVMs that jointly predict monthly gridded NBP and diagnose a latent active root-zone storage (aS_rz) state, while explicitly improving skill on climate extremes and disturbance events through weighted losses and auxiliary fire/drought inputs.

## Background
Pure CNN emulators of TRENDY models (Ke et al. arXiv:2611.04536) deliver strong global NBP skill with operational ERA5 forcing, yet grid-cell performance collapses under recursive prediction and remains weakest during extremes. The functionally accessible subsurface water (active root-zone storage aS_rz from Blougouras et al. WRR 2025WR042803) is not represented as an explicit state. This work embeds a differentiable ecohydrological module for latent aS_rz and adds extreme-aware losses and inputs.

## Key Components
- Hybrid CNN architecture with latent aS_rz state and mass-balance constraints
- Extreme- and disturbance-aware loss (weighted for large negative NBP anomalies)
- Auxiliary inputs: ERA5-FWI, MODIS/GFED burned area or emissions, VPD/SPEI
- Progressive autoregressive training for multi-year stability
- Evaluation on held-out years (2022-2024) and specific extreme events

## Data Sources
All public. See [docs/data_sources.md](docs/data_sources.md) for details and links.

## Expected Outcomes
Improved grid-scale skill under extremes, interpretable aS_rz diagnostics, low-latency carbon monitoring capability.

## Repository Structure
- `docs/` : Detailed proposal and data sources
- `src/` : Source code (to be developed)
- `notebooks/` : Analysis notebooks
- `configs/` : Configuration files
- `requirements.txt` : Python dependencies

## Setup
```bash
git clone https://github.com/murushyam/extreme-aware-hybrid-dgvm-emulators.git
cd extreme-aware-hybrid-dgvm-emulators
pip install -r requirements.txt
```

## License
MIT
