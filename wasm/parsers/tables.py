from typing import (
    IO,
    Type,
)

from wasm.datatypes import (
    FunctionAddress,
    Table,
    TableType,
)
from wasm.datatypes.valtype import ExternRef, FuncRef, RefType
from wasm.exceptions import (
    MalformedModule,
)
from wasm.instructions import Instruction
from wasm.instructions.table import ElemDrop, TableCopy, TableFill, TableGet, TableGrow, TableInit, TableSet, TableSize
from wasm.opcodes.binary import BinaryOpcode
from .indices import parse_elem_idx, parse_table_idx

from .byte import (
    parse_single_byte,
)
from .limits import (
    parse_limits,
)


def parse_table_element_type(stream: IO[bytes]) -> RefType:
    """
    Parse the element type for a TableType
    """
    type_flag = parse_single_byte(stream)

    if type_flag == 0x70:
        return FuncRef
    if type_flag == 0x6F:
        return ExternRef
    else:
        raise MalformedModule(
            f"Unrecognized table element type: {hex(type_flag)}"
        )


def parse_table_type(stream: IO[bytes]) -> TableType:
    """
    Parser for the TableType type
    """
    element_type = parse_table_element_type(stream)
    limits = parse_limits(stream)
    return TableType(limits, element_type)


def parse_table(stream: IO[bytes]) -> Table:
    """
    Parser for the Table type
    """
    table_type = parse_table_type(stream)
    return Table(table_type)


def parse_table_instruction(opcode: BinaryOpcode, stream: IO[bytes]) -> Instruction:
    if opcode is BinaryOpcode.TABLE_GET:
        tableidx = parse_table_idx(stream)
        return TableGet(tableidx)
    if opcode is BinaryOpcode.TABLE_SET:
        tableidx = parse_table_idx(stream)
        return TableSet(tableidx)
    if opcode is BinaryOpcode.TABLE_INIT:
        elemidx = parse_elem_idx(stream)
        tableidx = parse_table_idx(stream)
        return TableInit(tableidx, elemidx)
    if opcode is BinaryOpcode.ELEM_DROP:
        elemidx = parse_elem_idx(stream)
        return ElemDrop(elemidx)
    if opcode is BinaryOpcode.TABLE_COPY:
        tableidx1 = parse_table_idx(stream)
        tableidx2 = parse_table_idx(stream)
        return TableCopy(tableidx1, tableidx2)
    if opcode is BinaryOpcode.TABLE_GROW:
        tableidx = parse_table_idx(stream)
        return TableGrow(tableidx)
    if opcode is BinaryOpcode.TABLE_SIZE:
        tableidx = parse_table_idx(stream)
        return TableSize(tableidx)
    if opcode is BinaryOpcode.TABLE_FILL:
        tableidx = parse_table_idx(stream)
        return TableFill(tableidx)
    raise Exception(f"Invariant: got unknown opcode {opcode}")
    
    