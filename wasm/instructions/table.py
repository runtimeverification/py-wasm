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
    opcode: BinaryOpcode
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.opcode = BinaryOpcode.TABLE_GET
        self.tableidx = tableidx


    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableSet(Interned):
    opcode: BinaryOpcode
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.opcode = BinaryOpcode.TABLE_SET
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableSize(Interned):
    opcode: BinaryOpcode
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.opcode = BinaryOpcode.TABLE_SIZE
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableGrow(Interned):
    opcode: BinaryOpcode
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.opcode = BinaryOpcode.TABLE_GROW
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"


@register
class TableFill(Interned):
    opcode: BinaryOpcode
    tableidx: TableIdx

    def __init__(self, tableidx: TableIdx):
        self.opcode = BinaryOpcode.TABLE_FILL
        self.tableidx = tableidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx}"



@register
class TableCopy(Interned):
    opcode: BinaryOpcode
    tableidx1: TableIdx
    tableidx2: TableIdx

    def __init__(self, tableidx1: TableIdx, tableidx2: TableIdx):
        self.opcode = BinaryOpcode.TABLE_COPY
        self.tableidx1 = tableidx1
        self.tableidx2 = tableidx2

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx1} {self.tableidx2}"


@register
class TableInit(Interned):
    opcode: BinaryOpcode
    tableidx: TableIdx
    elemidx: ElemIdx

    def __init__(self, tableidx: TableIdx, elemidx: ElemIdx):
        self.opcode = BinaryOpcode.TABLE_INIT
        self.tableidx = tableidx
        self.elemidx = elemidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.tableidx} {self.elemidx}"
    

@register
class ElemDrop(Interned):
    opcode: BinaryOpcode
    elemidx: ElemIdx

    def __init__(self, elemidx: ElemIdx):
        self.opcode = BinaryOpcode.ELEM_DROP
        self.elemidx = elemidx

    def __str__(self) -> str:
        return f"{self.opcode.text} {self.elemidx}"
    
