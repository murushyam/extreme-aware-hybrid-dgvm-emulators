"""Training losses, including extreme- and disturbance-aware weighting.

TODO: implement an NBP loss that up-weights large negative anomalies,
plus optional mass-balance and aS_rz regularisation terms.
"""

from __future__ import annotations


def extreme_aware_nbp_loss(*args, **kwargs):
    """Placeholder for the weighted NBP loss.

    TODO:
        * Compute a base monthly NBP loss (for example, MSE).
        * Up-weight large negative NBP anomalies using a configurable
          threshold and weight (see configs/example_config.yaml).
        * Add mass-balance and aS_rz regularisation terms when enabled.
    """

    raise NotImplementedError(
        "extreme_aware_nbp_loss is a scaffold only; implementation will follow."
    )
