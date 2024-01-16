# Table Instructions
# https://webassembly.github.io/spec/core/syntax/instructions.html#table-instructions

from wasm._utils.interned import (
    Interned,
)
from wasm.datatypes.indices import ElemIdx, TableIdx
from wasm.opcodes import (
    BinaryOpcode,
)

from .base import (
    register,
)


@register
class TableGet(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_GET
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableSet(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_SET
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableSize(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_SIZE
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableGrow(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_GROW
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableFill(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_FILL
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"



@register
class TableCopy(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_COPY
    tableidx1: TableIdx
    tableidx2: TableIdx

    def __init__(self, tableidx1: TableIdx, tableidx2: TableIdx):
        self.tableidx1 = tableidx1
        self.tableidx2 = tableidx2

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx1} {self.tableidx2}"


@register
class TableInit(Interned):
    opcode: BinaryOpcode = BinaryOpcode.TABLE_INIT
    tableidx: TableIdx
    elemidx: ElemIdx

    def __init__(self, tableidx: TableIdx, elemidx: ElemIdx):
        self.tableidx = tableidx
        self.elemidx = elemidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx} {self.elemidx}"
    

@register
class ElemDrop(Interned):
    opcode: BinaryOpcode = BinaryOpcode.ELEM_DROP
    elemidx: ElemIdx

    def __init__(self, elemidx: ElemIdx):
        self.elemidx = elemidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.elemidx}"
    
