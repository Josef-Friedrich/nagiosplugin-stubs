from .compat import UserDict

class Cookie(UserDict):
    def __init__(self, statefile=...) -> None: ...
    def __enter__(self) -> Cookie: ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def open(self) -> Cookie: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
