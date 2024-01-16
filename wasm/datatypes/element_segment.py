from abc import ABC
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Iterable,
    NamedTuple,
    Tuple,
)

from wasm.datatypes.valtype import RefType

from .indices import (
    FunctionIdx,
    TableIdx,
)

if TYPE_CHECKING:
    from wasm.instructions import (  # noqa: F401
        BaseInstruction,
    )

class ElemMode(ABC):
    pass

@dataclass(frozen=True)
class ElemModeActive(ElemMode):
    table: TableIdx
    offset: Tuple['BaseInstruction', ...]


@dataclass(frozen=True)
class ElemModePassive(ElemMode):
    pass


@dataclass(frozen=True)
class ElemModeDeclarative(ElemMode):
    pass

class ElementSegment(NamedTuple):
    type: RefType
    init: Tuple[Iterable['BaseInstruction'], ...]
    mode: ElemMode
