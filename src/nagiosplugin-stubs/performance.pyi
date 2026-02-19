from typing import Any, Literal, NamedTuple, Optional

from .range import RangeSpec

def zap_none(val: Any | None) -> Any | Literal[""]: ...
def quote(label: str) -> str: ...

class Performance(
    NamedTuple(
        "Performance",
        [
            ("label", str),
            ("value", Any),
            ("uom", str),
            ("warn", RangeSpec),
            ("crit", RangeSpec),
            ("min", float),
            ("max", float),
        ],
    )
):
    def __new__(
        cls,
        label: str,
        value: Any,
        uom: Optional[str] = ...,
        warn: Optional[RangeSpec] = ...,
        crit: Optional[RangeSpec] = ...,
        min: Optional[float] = ...,
        max: Optional[float] = ...,
    ) -> Performance: ...
