"""Model components for the hybrid DGVM emulator.

TODO: implement a convolutional backbone, a differentiable latent aS_rz
module, and output heads for monthly NBP and aS_rz. Mass-balance
constraints should be applied in the state update, not as an afterthought.
"""

from __future__ import annotations


class HybridCNNDGVMEmulator:
    """Placeholder for the hybrid CNN with a latent aS_rz state.

    TODO:
        * Define the input stack (ERA5 climate, FWI, burned area or
          emissions, VPD/SPEI, optional ENSO, and lagged NBP).
        * Implement the convolutional encoder/decoder.
        * Implement the differentiable ecohydrological aS_rz update with
          mass-balance constraints.
        * Return monthly NBP and the updated latent aS_rz state.
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "HybridCNNDGVMEmulator is a scaffold only; implementation will follow."
        )
