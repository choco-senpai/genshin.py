"""ZZZ data overview models."""

import typing

import pydantic

from genshin.models.model import Aliased, APIModel

from ..character import ZZZPartialAgent

__all__ = (
    "HIACoin",
    "ZZZAreaCollection",
    "ZZZBangbooMicroWebBrief",
    "ZZZBaseBangboo",
    "ZZZCatNote",
    "ZZZChallengeSchedule",
    "ZZZClimbingTowerBrief",
    "ZZZClimbingTowerLayerInfo",
    "ZZZClimbingTowerMvpInfo",
    "ZZZClimbingTowerSeason",
    "ZZZGameData",
    "ZZZHadalBrief",
    "ZZZHadalBriefV2",
    "ZZZHoloBossBrief",
    "ZZZMedal",
    "ZZZProgressBrief",
    "ZZZRabBrief",
    "ZZZStats",
    "ZZZTempleData",
    "ZZZUserStats",
    "ZZZVoidFrontBrief",
)


class HIACoin(APIModel):
    """HIACoin model."""

    num: int
    name: str
    icon: str = Aliased("url")
    sort: typing.Optional[int] = None
    wiki_url: typing.Optional[str] = None


class ZZZProgressBrief(APIModel):
    """Generic current/max progress brief."""

    cur_progress: int = 0
    max_progress: int = 0


class ZZZBangbooMicroWebBrief(APIModel):
    """Bangboo micro web progress brief."""

    treasure_info: typing.Optional[ZZZProgressBrief] = None
    island_file: typing.Optional[ZZZProgressBrief] = None
    hot_event: typing.Optional[ZZZProgressBrief] = None
    level: int = 0


class ZZZClimbingTowerBrief(APIModel):
    """Simple climbing tower season brief (s2-style)."""

    climbing_tower_layer: int = 0
    floor_mvp_num: int = 0


class ZZZClimbingTowerLayerInfo(APIModel):
    """Climbing tower layer info."""

    climbing_tower_layer: int = 0
    total_score: int = 0
    icon: str = ""


class ZZZClimbingTowerMvpInfo(APIModel):
    """Climbing tower MVP info."""

    floor_mvp_num: int = 0
    rank_percent: int = 0
    display_rank: bool = False


class ZZZClimbingTowerSeason(APIModel):
    """Climbing tower season brief (s3/s4-style)."""

    layer_info: typing.Optional[ZZZClimbingTowerLayerInfo] = None
    mvp_info: typing.Optional[ZZZClimbingTowerMvpInfo] = None


class ZZZHadalBriefV2(APIModel):
    """Shiyu Defense (hadal) brief v2."""

    cur_period_zone_layer_count: int = 0
    score: int = 0
    rank_percent: int = 0
    rating: str = ""
    max_score: int = 0


class ZZZHadalBrief(APIModel):
    """Shiyu Defense (hadal) brief wrapper."""

    hadal_ver: str = ""
    hadal_brief_v2: typing.Optional[ZZZHadalBriefV2] = None


class ZZZVoidFrontBrief(APIModel):
    """Threshold Simulation (void front) overview brief."""

    void_front_id: int = 0
    has_ending_record: bool = False
    ending_record_name: str = ""
    total_score: int = 0
    rank_percent: int = 0


class ZZZTempleData(APIModel):
    """Suibian Temple overview data."""

    level: int = 0
    sell_days: int = 0
    total_sell_temple_coin: str = "0"


class ZZZRabBrief(APIModel):
    """RAB / climbing-related brief."""

    tower_flower: int = 0
    highest_score: int = 0
    rank: int = 0
    cur_stage: int = 0


class ZZZHoloBossBrief(APIModel):
    """Holo boss brief."""

    unlock: bool = False
    no_injured_boss_num: int = 0


class ZZZChallengeSchedule(APIModel):
    """Endgame challenge schedule entry."""

    challenge_type: str
    start_ts: str
    end_ts: str


class ZZZAreaCollection(APIModel):
    """Urban area collection progress."""

    urban_area_id: int
    urban_area_group_id: int
    is_lock: bool
    name: str
    icon: str
    collection_progress: int


class ZZZStats(APIModel):
    """ZZZ data overview stats."""

    active_days: int
    character_num: int = Aliased("avatar_num")
    inter_knot_reputation: str = Aliased("world_level_name")
    shiyu_defense_frontiers: int = Aliased("cur_period_zone_layer_count")
    bangboo_obtained: int = Aliased("buddy_num")
    achievement_count: int
    hia_coin: typing.Optional[HIACoin] = None
    commemorative_coins: typing.Sequence[HIACoin] = Aliased("commemorative_coins_list", default=())

    hadal_brief: typing.Optional[ZZZHadalBrief] = None
    void_front_brief: typing.Optional[ZZZVoidFrontBrief] = None
    climbing_tower_s2: typing.Optional[ZZZClimbingTowerBrief] = None
    climbing_tower_s3: typing.Optional[ZZZClimbingTowerSeason] = None
    climbing_tower_s4: typing.Optional[ZZZClimbingTowerSeason] = None
    climbing_tower_layer: typing.Optional[int] = None
    temple_data: typing.Optional[ZZZTempleData] = None
    rab_brief: typing.Optional[ZZZRabBrief] = None
    challenge_full_s_times: typing.Optional[int] = None
    memory_battlefield_full_stars_times: typing.Optional[int] = None
    next_hundred_layer: typing.Optional[str] = None
    stable_zone_layer_count: typing.Optional[int] = None
    bangboo_micro_web_brief: typing.Optional[ZZZBangbooMicroWebBrief] = None
    holo_boss_brief: typing.Optional[ZZZHoloBossBrief] = None

    @pydantic.model_validator(mode="before")
    @classmethod
    def __unnest_hia_coin(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        coins = values.get("commemorative_coins_list") or values.get("commemorative_coins") or []
        if "hia_coin" not in values:
            values["hia_coin"] = coins[0] if coins else None
        return values


class ZZZCatNote(APIModel):
    """ZZZ Cat note model."""

    icon: str
    id: int
    is_lock: bool
    name: str
    num: int
    total: int


class ZZZMedal(APIModel):
    """ZZZ player medal model."""

    icon: str = Aliased("medal_icon")
    number: int
    id: int = Aliased("medal_id")
    type: str = Aliased("medal_type")
    name: str
    is_show: bool
    no_injured: typing.Optional[bool] = None


class ZZZGameData(APIModel):
    """ZZZ game data model."""

    personal_title: str
    title_main_color: str
    title_bottom_color: str
    title_bg_url: str
    medal_icons: typing.Sequence[str] = Aliased("medal_list")
    card_url: str
    medals: typing.Sequence[ZZZMedal] = Aliased("all_medal_list")
    medal_item_list: typing.Sequence[ZZZMedal] = ()


class ZZZBaseBangboo(APIModel):
    """Base bangboo (buddy) model."""

    id: int
    name: str
    rarity: typing.Literal["S", "A"]
    level: int
    star: int
    bangboo_square_url: typing.Optional[str] = None
    bangboo_rectangle_url: typing.Optional[str] = None
    icon: str = ""

    @pydantic.model_validator(mode="before")
    @classmethod
    def __populate_icon(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        square = values.get("bangboo_square_url")
        rect = values.get("bangboo_rectangle_url")
        if not values.get("icon"):
            values["icon"] = square or rect or ""
        return values


class ZZZUserStats(APIModel):
    """Zenless Zone Zero user model."""

    stats: ZZZStats
    agents: typing.Sequence[ZZZPartialAgent] = Aliased("avatar_list")
    bangboos: typing.Sequence[ZZZBaseBangboo] = Aliased("buddy_list")
    in_game_avatar: str = Aliased("cur_head_icon_url")
    cat_notes: typing.Sequence[ZZZCatNote] = Aliased("cat_notes_list")
    in_game_data: ZZZGameData = Aliased("game_data_show")
    challenge_schedule_list: typing.Sequence[ZZZChallengeSchedule] = ()
    area_collections: typing.Sequence[ZZZAreaCollection] = ()
    award_state: typing.Optional[str] = None
