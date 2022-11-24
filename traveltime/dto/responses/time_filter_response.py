from dataclasses import dataclass
from typing import List, Optional

from traveltime.dto import SearchId, LocationId, Fares


@dataclass(frozen=True)
class DistanceBreakdown:
    mode: str
    distance: int


@dataclass(frozen=True)
class Property:
    travel_time: int
    distance: int
    distance_breakdown: List[DistanceBreakdown]
    fares: Optional[Fares]
    #route: Optional[Route] to be implemented


@dataclass(frozen=True)
class Location:
    id: LocationId
    properties: List[Property]


@dataclass(frozen=True)
class Result:
    search_id: SearchId
    unreachable: List[LocationId]


@dataclass(frozen=True)
class TimeFilterResponse:
    results: List[Result]
