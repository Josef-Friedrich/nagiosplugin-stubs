from typing import Callable, Iterator, Optional, Protocol

from nagiosplugin.metric import Metric
from nagiosplugin.performance import Performance
from nagiosplugin.range import RangOrString
from nagiosplugin.resource import Resource
from nagiosplugin.result import Result
from nagiosplugin.state import ServiceState

FmtMetric = str | Callable[[Metric, Context], str]

class ResultCls(Protocol):
    def __call__(
        self, state: ServiceState, hint: str | None = ..., metric: Metric | None = ...
    ) -> Result: ...

class Context:
    name: str
    fmt_metric: FmtMetric
    result_cls: ResultCls
    def __init__(
        self, name: str, fmt_metric: FmtMetric = ..., result_cls: ResultCls = ...
    ) -> None: ...
    def evaluate(self, metric: Metric, resource: Resource) -> Result: ...
    def performance(
        self, metric: Metric, resource: Resource
    ) -> Optional[Performance]: ...
    def describe(self, metric: Metric) -> str | None: ...

class ScalarContext(Context):
    def __init__(
        self,
        name: str,
        warning: RangOrString = ...,
        critical: RangOrString = ...,
        fmt_metric: FmtMetric = ...,
        result_cls: Result = ...,
    ) -> None: ...

class Contexts:
    by_name: dict[str, Context]

    def __init__(self) -> None: ...
    def add(self, context: Context) -> Context: ...
    def __getitem__(self, context_name: str) -> Context: ...
    def __contains__(self, context_name: str) -> Context: ...
    def __iter__(self) -> Iterator[Context]: ...
