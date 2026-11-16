# Detailed Research Proposal

## Title
Extreme-Aware Hybrid Emulators of Dynamic Global Vegetation Models with Latent Active Root-Zone Storage for Low-Latency Carbon Monitoring

## Objective
Develop hybrid convolutional emulators of TRENDY DGVMs that jointly predict monthly gridded NBP and diagnose a latent active root-zone storage (aS_rz) state, while explicitly improving skill on climate extremes and disturbance events through weighted losses and auxiliary fire/drought inputs. The resulting system will reduce recursive error accumulation, raise grid-scale anomaly skill during droughts, heatwaves and fires, and enable near-real-time diagnostic carbon budgets.

## Background and Motivation
Pure CNN emulators of TRENDY models (e.g., Ke et al. arXiv:2611.04536) deliver strong global NBP skill with operational ERA5 forcing, yet grid-cell performance collapses under recursive prediction and remains weakest during extremes. The functionally accessible subsurface water (active root-zone storage aS_rz from Blougouras et al. WRR 2025WR042803) is not represented as an explicit state. This work embeds a differentiable ecohydrological module for latent aS_rz and adds extreme-aware losses and inputs.

## Methods
- Hybrid CNN with latent aS_rz and mass-balance constraints
- Extreme-weighted loss for large negative anomalies
- Auxiliary inputs from FWI, burned area, VPD
- Progressive autoregressive training

## Data
See data_sources.md

## Evaluation
Held-out 2022-2024, extreme event skill scores, diagnostic aS_rz utility.

## Expected Contributions
Higher extreme skill, interpretable water-carbon states, low-latency capability.
