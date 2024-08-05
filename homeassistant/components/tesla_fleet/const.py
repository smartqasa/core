"""Constants used by Tesla Fleet integration."""

from __future__ import annotations

from enum import StrEnum
import logging

from tesla_fleet_api.const import Scope

DOMAIN = "tesla_fleet"

CONF_REFRESH_TOKEN = "refresh_token"

LOGGER = logging.getLogger(__package__)

SCOPES = [
    Scope.OPENID,
    Scope.OFFLINE_ACCESS,
    Scope.VEHICLE_DEVICE_DATA,
    Scope.VEHICLE_CMDS,
    Scope.VEHICLE_CHARGING_CMDS,
    Scope.ENERGY_DEVICE_DATA,
    Scope.ENERGY_CMDS,
]

MODELS = {
    "S": "Model S",
    "3": "Model 3",
    "X": "Model X",
    "Y": "Model Y",
}


class TeslaFleetState(StrEnum):
    """Teslemetry Vehicle States."""

    ONLINE = "online"
    ASLEEP = "asleep"
    OFFLINE = "offline"
