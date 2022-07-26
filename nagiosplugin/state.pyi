"""
This type stub file was generated by pyright.
"""

import collections

"""Classes  to represent check outcomes.

This module defines :class:`ServiceState` which is the abstract base class
for check outcomes. The four states defined by the :term:`Nagios plugin API`
are represented as singleton subclasses.

Note that the *warning* state is defined by the :class:`Warn` class. The
class has not been named `Warning` to avoid being confused with the
built-in Python exception of the same name.
"""

def worst(states):
    """Reduce list of *states* to the most significant state."""
    ...

class ServiceState(collections.namedtuple("ServiceState", "code text")):
    """Abstract base class for all states.

    Each state has two constant attributes: :attr:`text` is the short
    text representation which is printed for example at the beginning of
    the summary line. :attr:`code` is the corresponding exit code.
    """

    def __str__(self) -> str:
        """Plugin-API compliant text representation."""
        ...
    def __int__(self) -> int:
        """Plugin API compliant exit code."""
        ...

class Ok(ServiceState):
    def __new__(cls): ...

Ok = ...

class Warn(ServiceState):
    def __new__(cls): ...

Warn = ...

class Critical(ServiceState):
    def __new__(cls): ...

Critical = ...

class Unknown(ServiceState):
    def __new__(cls): ...

Unknown = ...
