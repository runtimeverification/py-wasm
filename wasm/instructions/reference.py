# Reference Instructions
# https://webassembly.github.io/spec/core/syntax/instructions.html#reference-instructions
#

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
    opcode: BinaryOpcode = BinaryOpcode.REF_NULL
    reftype: RefType

    def __init__(self, reftype: RefType):
        self.reftype = reftype

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.reftype}]"


@register
class RefIsNull(Interned):
    opcode: BinaryOpcode = BinaryOpcode.REF_IS_NULL

    def __init__(self):
        return
        
    def __str__(self) -> str:
        return f"{self.opcode.text}"


@register
class RefFunc(Interned):
    opcode: BinaryOpcode = BinaryOpcode.REF_FUNC
    funcidx: FunctionIdx

    def __init__(self, funcidx: FunctionIdx):
        self.funcidx = funcidx
  
    def __str__(self) -> str:
        return f"{self.opcode.text} {self.funcidx}]"
