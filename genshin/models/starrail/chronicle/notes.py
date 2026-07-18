"""Starrail chronicle notes."""

import datetime
import typing

from genshin.models.model import Aliased, APIModel

__all__ = ["StarRailExpedition", "StarRailNote"]


class StarRailExpedition(APIModel):
    """StarRail expedition."""

    avatars: list[str]
    status: typing.Literal["Ongoing", "Finished"]
    remaining_time: datetime.timedelta
    name: str
    item_url: str

    @property
    def finished(self) -> bool:
        """Whether the expedition has finished."""
        return self.remaining_time <= datetime.timedelta(0)

    @property
    def completion_time(self) -> datetime.datetime:
        return datetime.datetime.now().astimezone() + self.remaining_time


class StarRailNote(APIModel):
    """StarRail chronicle note."""

    current_stamina: int
    max_stamina: int
    stamina_recover_time: datetime.timedelta
    accepted_expedition_num: int = Aliased("accepted_epedition_num")
    total_expedition_num: int
    expeditions: typing.Sequence[StarRailExpedition]

    current_train_score: int
    """Current daily training activity"""
    max_train_score: int
    """Max daily training activity"""

    current_rogue_score: int
    """Current simulated universe weekly points"""
    max_rogue_score: int
    """Max simulated universe weekly points"""

    have_bonus_synchronicity_points: bool = Aliased("rogue_tourn_weekly_unlocked")
    """Whether the Divergent Universe is unlocked"""
    max_bonus_synchronicity_points: int = Aliased("rogue_tourn_weekly_max")
    """The max number of this week's Bonus Synchronicity Points"""
    current_bonus_synchronicity_points: int = Aliased("rogue_tourn_weekly_cur")
    """The current number of this week's Bonus Synchronicity Points"""

    remaining_weekly_discounts: int = Aliased("weekly_cocoon_cnt")
    """Remaining echo of war rewards"""
    max_weekly_discounts: int = Aliased("weekly_cocoon_limit")
    """Echo of war attempt limit"""

    current_reserve_stamina: int
    is_reserve_stamina_full: bool

    grid_fight_weekly_max: typing.Optional[int] = None
    """Max weekly Grid Fight score."""
    grid_fight_weekly_cur: typing.Optional[int] = None
    """Current weekly Grid Fight score."""
    period_max_score: typing.Optional[int] = None
    period_score: typing.Optional[int] = None
    stamina_full_ts: typing.Optional[int] = None
    """Unix timestamp when stamina will be full."""
    current_ts: typing.Optional[int] = None
    rogue_tourn_exp_is_full: typing.Optional[bool] = None

    @property
    def stamina_recovery_time(self) -> datetime.datetime:
        """The time when stamina will be recovered."""
        return datetime.datetime.now().astimezone() + self.stamina_recover_time
