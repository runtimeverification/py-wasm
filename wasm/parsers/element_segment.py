from typing import IO, Iterable, cast

from wasm.datatypes import ElementSegment
from wasm.datatypes.element_segment import ElemModeActive, ElemModeDeclarative, ElemModePassive
from wasm.datatypes.indices import FunctionIdx, TableIdx
from wasm.datatypes.valtype import FunctionAddress, RefType
from wasm.instructions.base import BaseInstruction
from wasm.instructions.reference import RefFunc
from wasm.parsers.integers import parse_u32
from wasm.parsers.null import parse_null_byte
from wasm.parsers.valtype import parse_reftype

from .expressions import parse_expression
from .indices import parse_function_idx, parse_table_idx
from .vector import parse_vector


def parse_element_kind(stream: IO[bytes]) -> RefType:
    parse_null_byte(stream)
    return FunctionAddress


def parse_element_segment(stream: IO[bytes]) -> ElementSegment:
    """
    Parser for the ElementSegment type.
    """

    def idxs_to_exprs(idxs: Iterable[FunctionIdx]) -> tuple[Iterable[BaseInstruction], ...]:
        def idx_to_instr(i: FunctionIdx) -> BaseInstruction:
            instr = RefFunc(i)
            return cast(BaseInstruction, instr)

        return tuple((idx_to_instr(i),) for i in idxs)

    choice = parse_u32(stream)

    if choice == 0:
        offset = parse_expression(stream)
        idxs = parse_vector(parse_function_idx, stream)
        init = idxs_to_exprs(idxs)
        mode = ElemModeActive(TableIdx(0), offset)
        return ElementSegment(FunctionAddress, init, mode)
    if choice == 1:
        type = parse_element_kind(stream)
        idxs = parse_vector(parse_function_idx, stream)
        init = idxs_to_exprs(idxs)
        return ElementSegment(type, init, ElemModePassive())
    if choice == 2:
        table_idx = parse_table_idx(stream)
        offset = parse_expression(stream)
        type = parse_element_kind(stream)
        idxs = parse_vector(parse_function_idx, stream)
        init = idxs_to_exprs(idxs)
        mode = ElemModeActive(table_idx, offset)
        return ElementSegment(type, init, mode)
    if choice == 3:
        type = parse_element_kind(stream)
        idxs = parse_vector(parse_function_idx, stream)
        init = idxs_to_exprs(idxs)
        return ElementSegment(type, init, ElemModeDeclarative())
    if choice == 4:
        offset = parse_expression(stream)
        init = parse_vector(parse_expression, stream)
        mode = ElemModeActive(TableIdx(0), offset)
        return ElementSegment(FunctionAddress, init, mode)
    if choice == 5:
        type = parse_reftype(stream)
        init = parse_vector(parse_expression, stream)
        return ElementSegment(type, init, ElemModePassive())
    if choice == 6:
        table_idx = parse_table_idx(stream)
        offset = parse_expression(stream)
        type = parse_reftype(stream)
        init = parse_vector(parse_expression, stream)
        mode = ElemModeActive(table_idx, offset)
        return ElementSegment(type, init, mode)
    if choice == 7:
        type = parse_reftype(stream)
        init = parse_vector(parse_expression, stream)
        return ElementSegment(type, init, ElemModeDeclarative())
    raise ValueError(f'ElementSegment parser not implemented: {choice}')
