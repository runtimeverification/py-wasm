import enum
from typing import NamedTuple

from wasm._utils.interned import (
    Interned,
)
from wasm.datatypes import (
    GlobalIdx,
    LocalIdx,
)
from wasm.datatypes.indices import FunctionIdx
from wasm.datatypes.valtype import RefType
from wasm.opcodes import (
    BinaryOpcode,
)

from .base import (
    register,
)


@register
class RefNull(Interned):
    opcode: BinaryOpcode
    reftype: RefType

    def __init__(self, reftype: RefType):
        self.opcode = BinaryOpcode.REF_FUNC
        self.reftype = RefType

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.reftype}]"


@register
class RefIsNull(Interned):
    opcode: BinaryOpcode

    def __init__(self):
        self.opcode = BinaryOpcode.REF_IS_NULL
        
    def __str__(self) -> str:
        return f"{self.opcode.text}"


@register
class RefFunc(Interned):
    opcode: BinaryOpcode
    funcidx: FunctionIdx

    def __init__(self, funcidx: FunctionIdx):
        self.opcode = BinaryOpcode.REF_FUNC
        self.funcidx = funcidx
  
    def __str__(self) -> str:
        return f"{self.opcode.text} {self.funcidx}]"
