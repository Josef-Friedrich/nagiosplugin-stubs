from typing import Generator, Union

from nagiosplugin.metric import Metric

class Resource:
    name: str

    def probe(self) -> Union[list[Metric], Metric, Generator[Metric, None, None]]: ...
