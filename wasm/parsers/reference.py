from typing import IO

from wasm.instructions import Instruction
from wasm.instructions.reference import RefFunc, RefIsNull, RefNull
from wasm.opcodes import BinaryOpcode
from wasm.parsers.indices import parse_function_idx
from wasm.parsers.valtype import parse_reftype


def parse_reference_instruction(opcode: BinaryOpcode, stream: IO[bytes]) -> Instruction:
    if opcode is BinaryOpcode.REF_NULL:
        reftype = parse_reftype(stream)
        return RefNull(reftype)
    if opcode is BinaryOpcode.REF_IS_NULL:
        return RefIsNull()
    if opcode is BinaryOpcode.REF_FUNC:
        funcidx = parse_function_idx(stream)
        return RefFunc(funcidx)
    raise Exception(f"Invariant: got unknown opcode {opcode}")
