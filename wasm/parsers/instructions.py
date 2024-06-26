from typing import IO

from wasm.exceptions import (
    MalformedModule,
)
from wasm.instructions import (
    Instruction,
)
from wasm.opcodes import (
    BinaryOpcode,
)
from .integers import parse_u32
from .tables import parse_table_instruction
from .reference import parse_reference_instruction

from .control import (
    parse_control_instruction,
)
from .memory import (
    parse_memory_instruction,
)
from .numeric import (
    parse_numeric_instruction,
)
from .parametric import (
    parse_parametric_instruction,
)
from .variable import (
    parse_variable_instruction,
)


def parse_instruction(stream: IO[bytes]) -> Instruction:
    """
    Parse a single instruction.
    """
    opcode_byte = stream.read(1)

    try:
        opcode_value = opcode_byte[0]
    except IndexError:
        raise Exception("TODO: end of stream, what is the right exception here")

    # '0xFC' is a special opcode shared by several instructions.
    # These instructions are distinguished by a u32 value following the opcode.
    if opcode_value == 0xFC:
        try:
            additional_value = parse_u32(stream)
            opcode_value = (opcode_value << 32) + additional_value
        except IndexError:
            raise Exception("TODO: cannot parse opcode, expected u32 after 0xFC")
        
    try:
        opcode = BinaryOpcode(opcode_value)
    except ValueError:
        raise MalformedModule(
            f"Unknown opcode: {hex(opcode_value)} found at position {stream.tell() - 1}"
        )

    if opcode.is_numeric:
        return parse_numeric_instruction(opcode, stream)
    elif opcode.is_variable:
        return parse_variable_instruction(opcode, stream)
    elif opcode.is_memory:
        return parse_memory_instruction(opcode, stream)
    elif opcode.is_parametric:
        return parse_parametric_instruction(opcode, stream)
    elif opcode.is_control:
        return parse_control_instruction(opcode, stream)
    elif opcode.is_reference:
        return parse_reference_instruction(opcode, stream)
    elif opcode.is_table:
        return parse_table_instruction(opcode, stream)
    else:
        raise Exception(f"Unhandled opcode: {opcode}")
