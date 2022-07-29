from dataclasses import dataclass
from typing import Any

from nagiosplugin.context import Context
from nagiosplugin.performance import Performance
from nagiosplugin.resource import Resource
from nagiosplugin.result import Result
from typing_extensions import TypedDict, Unpack

class MetricKwargs(TypedDict, total=False):
    name: str
    value: Any
    uom: str
    min: int | float
    max: int | float
    context: str
    contextobj: Context
    resource: Resource

@dataclass
class Metric:

    name: str
    value: Any
    uom: str | None = None
    min: int | float | None = None
    max: int | float | None = None
    context: str | None = None
    contextobj: Context | None = None
    resource: Resource | None = None

    def replace(self, **attr: Unpack[MetricKwargs]) -> Metric: ...
    @property
    def description(self) -> str: ...
    @property
    def valueunit(self) -> str: ...
    def evaluate(self) -> Result: ...
    def performance(self) -> Performance: ...
