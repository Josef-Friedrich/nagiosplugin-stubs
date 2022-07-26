from typing import Generator, List

from nagiosplugin.metric import Metric

class Resource:

    name: str

    def probe(self) -> List[Metric] | Metric | Generator[Metric, None, None]: ...
