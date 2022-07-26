from dataclasses import dataclass
from typing import Any

from nagiosplugin.context import Context
from nagiosplugin.performance import Performance
from nagiosplugin.resource import Resource
from nagiosplugin.result import Result

@dataclass
class Metric:

    name: str | None
    value: Any | None
    uom: str | None = None
    min: int | float | None = None
    max: int | float | None = None
    context: str | None = None
    contextobj: Context | None = None
    resource: Resource | None = None

    def replace(self, **attr) -> Metric: ...
    @property
    def description(self) -> str: ...
    @property
    def valueunit(self) -> str: ...
    def evaluate(self) -> Result: ...
    def performance(self) -> Performance: ...
