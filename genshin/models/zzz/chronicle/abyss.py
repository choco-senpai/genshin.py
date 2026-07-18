"""Hollow Zero models."""

import datetime
import typing
from enum import IntEnum

from genshin.models.model import Aliased, APIModel

__all__ = (
    "LostVoidCommissionProgress",
    "LostVoidData",
    "LostVoidDataType",
    "LostVoidExplorationLog",
    "LostVoidLicense",
    "LostVoidSpecialMission",
    "LostVoidSummary",
    "LostVoidTaskForceInvestigation",
    "LostVoidUltimateChallenge",
)


class LostVoidLicense(APIModel):
    """Lost void license model."""

    cur_level: int
    max_level: int
    icon: str


class LostVoidExplorationLog(APIModel):
    """Lost void exploration log model."""

    current: int = Aliased("cur_task")
    total: int = Aliased("max_task")


class LostVoidCommissionProgress(APIModel):
    """Lost void bounty commission progress model."""

    current: int = Aliased("cur_duty")
    total: int = Aliased("max_duty")


class LostVoidUltimateChallenge(APIModel):
    """Lost void ultimate challenge model."""

    highest_difficulty: str = Aliased("max_name")
    """Highest Difficulty Cleared."""
    total_clears: int = Aliased("max_count")
    """Total Clears on the Highest Difficulty Completed."""
    shortest_clear_time: datetime.timedelta = Aliased("best_time")
    """Shortest Clear Time on the Highest Difficulty Completed."""

    has_data: bool
    heat_count: typing.Optional[int] = None


class LostVoidTaskForceInvestigation(APIModel):
    """Lost void task force investigation max record."""

    max_name: str = ""
    heat_count: int = 0
    max_count: int = 0
    best_time: datetime.timedelta = datetime.timedelta()
    has_data: bool = False


class LostVoidSpecialMission(APIModel):
    """Lost void special mission record."""

    has_data: bool = False
    heat_count: int = 0
    high_difficulty: int = 0
    max_count: int = 0
    best_time: datetime.timedelta = datetime.timedelta()


class LostVoidDataType(IntEnum):
    """Lost void data type enum."""

    EXPLORERS_BADGE = 1
    GEAR_DATABASE = 2
    RESONIUM_RESEARCH = 3
    CARD_DATABASE = 4
    TACTICAL_PRISM_PROGRAM = 5
    UNOFFICIAL_GUIDE = 6
    AUXILLARY_GEAR_DATABASE = 7


class LostVoidData(APIModel):
    """Lost void data model."""

    type: LostVoidDataType
    collected: int = Aliased("cur_collect")
    total: int = Aliased("max_collect")


class LostVoidSummary(APIModel):
    """Lost void summary model."""

    time_remaining: datetime.timedelta = Aliased("refresh_time")
    unlocked: bool = Aliased("unlock")

    license: LostVoidLicense = Aliased("abyss_level")
    exploration_log: LostVoidExplorationLog = Aliased("abyss_task")
    commission_progress: LostVoidCommissionProgress = Aliased("abyss_duty")
    ultimate_challenge: LostVoidUltimateChallenge = Aliased("abyss_max")
    data_collected: typing.Sequence[LostVoidData] = Aliased("abyss_collect")
    abyss_task_force_investigation_max: typing.Optional[LostVoidTaskForceInvestigation] = None
    special_mission: typing.Optional[LostVoidSpecialMission] = None
