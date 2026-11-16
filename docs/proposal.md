# Extreme-Aware Hybrid Emulators of Dynamic Global Vegetation Models with Latent Active Root-Zone Storage for Low-Latency Carbon Monitoring

**Author:** Shyam Sunder Murugesan Sellammal, NIT Rourkela  
**ORCID:** [0000-0002-9964-6199](https://orcid.org/0000-0002-9964-6199)

This document is a research-design note for an early-stage project. It expands the summary in the repository README. It does not report completed experiments or fitted results.

## Objective

The aim is to develop hybrid convolutional emulators of TRENDY dynamic global vegetation models (DGVMs) that jointly predict monthly gridded net biome production (NBP) and diagnose a latent active root-zone storage (aS_rz) state. Skill on climate extremes and disturbance events will be improved explicitly, through weighted losses and auxiliary fire and drought inputs.

If successful, the system will reduce recursive error accumulation, raise grid-scale anomaly skill during droughts, heatwaves and fires, and enable near-real-time diagnostic carbon budgets.

## Background and Motivation

The Global Carbon Budget estimates the land carbon sink with an ensemble of DGVMs in the TRENDY project. Those simulations are typically completed once a year, after the climate forcing for the previous year becomes available. Convolutional neural network (CNN) emulators can be driven by operational reanalysis and, in principle, can produce DGVM-consistent NBP with much lower latency.

Ke et al. (arXiv:2611.04536) trained CNN emulators of TRENDY models and showed strong global NBP skill with ERA5 forcing. The same study found that grid-cell performance is much weaker under recursive prediction, in part because errors accumulate in the emulated NBP history, and that skill remains poorest during extremes. Pure CNN emulators also do not carry an explicit state for the functionally accessible subsurface water that ecosystems can use.

Blougouras et al. (Water Resources Research, 2025WR042803) define active root-zone storage, aS_rz, as a time-varying latent state for that accessible water. This project takes that idea into a DGVM-emulator setting. A differentiable ecohydrological module will represent latent aS_rz, and extreme-aware losses and inputs will be added so that the emulator is not trained only on average monthly behaviour.

## Research Questions

The work is organised around three questions that follow directly from the objective:

1. Can a hybrid CNN, with a latent aS_rz state and mass-balance constraints, reduce recursive error accumulation relative to a pure CNN emulator of TRENDY monthly NBP?
2. Do extreme- and disturbance-aware loss weights, together with auxiliary fire and drought inputs, raise grid-scale anomaly skill during droughts, heatwaves and fires?
3. Can the trained system yield interpretable aS_rz diagnostics and a low-latency, diagnostic carbon-budget workflow that can be updated as operational climate and fire data arrive?

These are questions to be tested. They are not claims of results.

## Methodology

### Hybrid CNN with latent aS_rz and mass-balance constraints

The core model is a convolutional emulator of TRENDY NBP. In addition to a monthly NBP output, the network will maintain a latent aS_rz state. A differentiable ecohydrological module will update that state from climate inputs and from the network's own diagnosed fluxes, subject to mass-balance constraints of the form used to define aS_rz (storage change related to effective water input and evapotranspiration). The aS_rz state is intended to carry memory of accessible subsurface water across months, rather than leaving all memory in a purely statistical lag of past NBP.

Exact layer widths, input stacks and constraint weights are not fixed in this note. Placeholders are recorded in `configs/example_config.yaml`.

### Extreme- and disturbance-aware loss

Training will use a loss on monthly NBP that up-weights large negative anomalies. The goal is to spend more of the learning signal on drought, heat and fire-related carbon drawdowns, which is where pure emulators have been weakest. The precise threshold and weight are hyperparameters, not fitted values, and will be selected on a validation period.

### Auxiliary inputs

Alongside standard ERA5 climate forcing, the emulator will ingest variables that describe fire weather, burned area or fire emissions, and atmospheric or drought stress:

- ERA5-based Fire Weather Index (FWI) and, where useful, related fire-danger indices
- MODIS MCD64A1 burned area, or GFED5 / GFED5 near-real-time burned area or emissions
- Vapour pressure deficit (VPD) derived from ERA5 temperature and dewpoint, and/or SPEI

An ENSO index (ONI or Niño 3.4) may be included as a large-scale context variable. Official sources for each dataset are listed in [data_sources.md](data_sources.md).

### Progressive autoregressive training

At inference time the emulator will be run recursively, feeding its own past NBP (and the latent aS_rz state) forward over many months. To improve multi-year stability, training will move gradually from short, teacher-forced windows to longer autoregressive rollouts. The schedule is a design choice to be refined; an example is given in the configuration file.

## Evaluation

The planned evaluation uses years that are held out from training:

- Held-out period: 2022-2024, subject to the coverage of the TRENDY release in use.
- Metrics: grid-scale anomaly skill (for example, anomaly R-squared and error statistics for monthly NBP), global and regional aggregates, and skill stratified on droughts, heatwaves and fires.
- Recursive stability: multi-year rollouts in which the emulator is driven by its own previous predictions, with attention to error accumulation.
- Event case studies: specific extreme events, to be listed once the study period and event catalogue are fixed.

No scores are reported here. Baseline comparisons will include a pure CNN emulator trained under the same data splits, in the spirit of Ke et al. (2026), so that the contribution of the latent aS_rz module, the weighted loss and the auxiliary inputs can be isolated.

## Data

All source datasets are public. The working list is:

- TRENDY S2 and S3 gridded NBP, accessed through the Global Carbon Budget TRENDY distribution
- ERA5 climate and the CEMS ERA5-based fire danger indices (FWI)
- MODIS MCD64A1 burned area, and GFED5 plus GFED5 near-real-time products
- VPD derived from ERA5, SPEI from SPEIbase, and an ENSO index from NOAA

Resolution, period and access notes are collected in [data_sources.md](data_sources.md). Use of TRENDY output is subject to the data policy of the relevant Global Carbon Budget / TRENDY release. Local NetCDF, Zarr and model checkpoints are not stored in this repository.

## Expected Outcomes

- Higher grid-scale NBP anomaly skill under droughts, heatwaves and fires, relative to a pure CNN baseline trained on the same splits.
- Lower recursive error accumulation in multi-year autoregressive rollouts.
- Interpretable aS_rz diagnostics that can be inspected alongside NBP.
- A low-latency workflow for diagnostic carbon monitoring, once operational climate and fire inputs are in place.

These are target outcomes. They will be accepted or revised according to the evaluation above.

## Workplan

A detailed workplan, with dates and deliverables, will be added as data access and compute are confirmed. The intended sequence is:

1. Assemble and preprocess TRENDY NBP, ERA5 climate and FWI, burned-area or emissions products, and drought or climate-mode indices.
2. Implement a baseline pure CNN emulator and the training, validation and 2022-2024 test splits.
3. Add the hybrid architecture, the latent aS_rz module and mass-balance constraints.
4. Introduce extreme- and disturbance-aware losses and the auxiliary fire and drought inputs.
5. Apply progressive autoregressive training and evaluate recursive stability, grid-scale anomaly skill and selected extreme events.

This outline is a planning placeholder, not a commitment to a calendar.

## References

Ke, P., Gui, X., Sitch, S., Liu, Z., Li, X., Bian, J., Friedlingstein, P., and Ciais, P. (2026). Machine learning emulators of dynamic global vegetation models for fast gridded carbon budget predictions. arXiv:2611.04536. https://doi.org/10.48550/arXiv.2611.04536

Blougouras, G., Jiang, S., Brenning, A., Migliavacca, M., Slater, L., Zhou, J., Kumar, R., Tian, L., Wang, C., and Reichstein, M. (2026). Spatiotemporal dynamics of active root zone storage revealed from hybrid machine learning. *Water Resources Research*, 62, e2025WR042803. https://doi.org/10.1029/2025WR042803
