from typing import Any, Literal, NamedTuple, Optional

from .range import RangeOrString

def zap_none(val: Any | None) -> Any | Literal[""]: ...
def quote(label: str) -> str: ...

class Performance(
    NamedTuple(
        "Performance",
        [
            ("label", str),
            ("value", Any),
            ("uom", str),
            ("warn", RangeOrString),
            ("crit", RangeOrString),
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
        warn: Optional[RangeOrString] = ...,
        crit: Optional[RangeOrString] = ...,
        min: Optional[float] = ...,
        max: Optional[float] = ...,
    ) -> Performance: ...
