from dataclasses import dataclass
from typing import Any, Literal

def zap_none(val: Any | None) -> Any | Literal[""]: ...
def quote(label: str) -> str: ...
@dataclass
class Performance:

    label: str
    value: Any
    uom: str | None = None
    warn: int | float | None = None
    crit: int | float | None = None
    min: int | float | None = None
    max: int | float | None = None

    def __str__(self) -> str: ...
