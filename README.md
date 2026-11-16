# Extreme-Aware Hybrid Emulators of Dynamic Global Vegetation Models with Latent Active Root-Zone Storage for Low-Latency Carbon Monitoring

This repository develops hybrid convolutional emulators of TRENDY dynamic global vegetation models (DGVMs). The emulators jointly predict monthly gridded net biome production (NBP) and diagnose a latent active root-zone storage (aS_rz) state. Weighted losses and auxiliary fire and drought inputs are used to improve skill during climate extremes and disturbance events. The intended outcome is a system that reduces recursive error accumulation, raises grid-scale anomaly skill during droughts, heatwaves and fires, and supports near-real-time diagnostic carbon budgets.

**Status:** early-stage research project; code to follow.

**Author:** Shyam Sunder Murugesan Sellammal, NIT Rourkela  
**ORCID:** [0000-0002-9964-6199](https://orcid.org/0000-0002-9964-6199)

A longer account of the research design is in [docs/proposal.md](docs/proposal.md). Dataset access notes and official links are in [docs/data_sources.md](docs/data_sources.md).

## Objective

Develop hybrid convolutional emulators of TRENDY DGVMs that jointly predict monthly gridded NBP and diagnose a latent active root-zone storage (aS_rz) state, while explicitly improving skill on climate extremes and disturbance events through weighted losses and auxiliary fire and drought inputs. The resulting system will reduce recursive error accumulation, raise grid-scale anomaly skill during droughts, heatwaves and fires, and enable near-real-time diagnostic carbon budgets.

## Background and Motivation

Pure CNN emulators of TRENDY models (for example, Ke et al., arXiv:2611.04536) deliver strong global NBP skill with operational ERA5 forcing. Grid-cell performance is much weaker under recursive prediction, and skill remains poorest during extremes. Functionally accessible subsurface water, the active root-zone storage aS_rz described by Blougouras et al. (Water Resources Research, 2025WR042803), is not represented as an explicit state in those emulators. This work embeds a differentiable ecohydrological module for latent aS_rz and adds extreme-aware losses and inputs.

## Key Components

- Hybrid CNN architecture with a latent aS_rz state and mass-balance constraints.
- Extreme- and disturbance-aware loss, weighted for large negative NBP anomalies.
- Auxiliary inputs: ERA5-based Fire Weather Index (FWI), MODIS or GFED burned area or emissions, and VPD or SPEI.
- Progressive autoregressive training for multi-year stability.
- Evaluation on held-out years (2022-2024) and on specific extreme events.

## Data Sources

All source datasets are public. See [docs/data_sources.md](docs/data_sources.md) for official links, variables and access notes.

- TRENDY S2/S3 NBP
- ERA5 climate and ERA5-based FWI
- MODIS MCD64A1 burned area, and GFED5 plus GFED5 near-real-time products
- Supporting indices: vapour pressure deficit (VPD), SPEI, and ENSO (ONI / Niño 3.4)

## Expected Outcomes

Improved grid-scale skill under extremes, interpretable aS_rz diagnostics, and a low-latency carbon monitoring capability.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── configs/
│   └── example_config.yaml
├── docs/
│   ├── proposal.md
│   └── data_sources.md
├── notebooks/
│   └── README.md
└── src/
    └── dgvm_emulator/
        ├── README.md
        ├── __init__.py
        ├── models.py
        ├── losses.py
        └── data.py
```

## Setup

Python 3.10 or later is recommended. System libraries required by Cartopy (PROJ and GEOS) should be installed through your package manager or conda if map plots are needed.

### Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

If you plan to train on a GPU, install a CUDA build of PyTorch from the [official PyTorch instructions](https://pytorch.org/get-started/locally/) before, or instead of, the unpinned `torch` line in `requirements.txt`.

### Conda

```bash
conda create -n dgvm-emulator python=3.11
conda activate dgvm-emulator
pip install -r requirements.txt
```

The package currently lives under `src/`. From the repository root you can add it to the import path with:

```bash
export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
```

An example configuration, including a held-out test period of 2022-2024, is in `configs/example_config.yaml`. Paths and hyperparameters in that file are placeholders.

## References

Ke, P., Gui, X., Sitch, S., Liu, Z., Li, X., Bian, J., Friedlingstein, P., and Ciais, P. (2026). Machine learning emulators of dynamic global vegetation models for fast gridded carbon budget predictions. arXiv:2611.04536. https://doi.org/10.48550/arXiv.2611.04536

Blougouras, G., Jiang, S., Brenning, A., Migliavacca, M., Slater, L., Zhou, J., Kumar, R., Tian, L., Wang, C., and Reichstein, M. (2026). Spatiotemporal dynamics of active root zone storage revealed from hybrid machine learning. *Water Resources Research*, 62, e2025WR042803. https://doi.org/10.1029/2025WR042803

## License

This project is released under the [MIT License](LICENSE). Copyright (c) 2026 Shyam Sunder Murugesan Sellammal.
