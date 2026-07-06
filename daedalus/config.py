"""Basic configuration defaults for Daedalus CLI."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DaedalusConfig:
    """Default Daedalus CLI configuration."""

    author: str = "Daedalus"
    default_status: str = "Proposed"
    default_risk_level: str = "Low"


DEFAULT_CONFIG = DaedalusConfig()
