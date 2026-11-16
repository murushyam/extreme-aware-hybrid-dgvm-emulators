"""Dataset loading and preprocessing for TRENDY, ERA5 and auxiliary fields.

TODO: read official products described in docs/data_sources.md, align them
on a common grid and monthly calendar, derive VPD from ERA5 temperature
and dewpoint, and build training, validation and 2022-2024 test splits.
"""

from __future__ import annotations


class DGVMEmulatorDataset:
    """Placeholder for the gridded training dataset.

    TODO:
        * Load TRENDY S2/S3 NBP and ERA5 climate.
        * Load FWI, burned area or emissions, SPEI and an ENSO index.
        * Derive VPD from ERA5 2 m temperature and dewpoint.
        * Honour the year splits in the configuration file.
        * Yield input stacks and NBP targets without leaking test years.
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "DGVMEmulatorDataset is a scaffold only; implementation will follow."
        )
