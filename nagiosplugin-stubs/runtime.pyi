from io import StringIO
from logging import StreamHandler
from typing import NoReturn

from nagiosplugin.check import Check
from nagiosplugin.output import Output

def guarded(original_function=..., verbose: bool = ...): ...

class Runtime:
    instance: Runtime = ...
    check: Check = ...
    _verbose: int = ...
    timeout: int = ...
    logchan: StreamHandler[StringIO] = ...
    output: Output = ...
    stdout = ...
    exitcode: int = ...
    def __new__(cls) -> Runtime: ...
    def __init__(self) -> None: ...
    @property
    def verbose(self) -> int: ...
    @verbose.setter
    def verbose(self, verbose: int) -> None: ...
    def run(self, check: Check) -> None: ...
    def execute(
        self, check: Check, verbose: bool = ..., timeout: int = ...
    ) -> NoReturn: ...
    def sysexit(self) -> NoReturn: ...
