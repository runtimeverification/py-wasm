from typing import IO

from wasm.datatypes import (
    RefType,
    ValType,
)
from wasm.exceptions import (
    MalformedModule,
)

from .byte import (
    parse_single_byte,
)


def parse_valtype(stream: IO[bytes]) -> ValType:
    """
    Parser for the ValType type
    """
    byte = parse_single_byte(stream)

    try:
        return ValType.from_byte(byte)
    except ValueError as err:
        raise MalformedModule(
            f"Invalid byte while parsing valtype.  Got '{hex(byte)}: {str(err)}"
        )

def parse_reftype(stream) -> ValType:
    valtype = parse_valtype(stream)
    if valtype.is_reference_type:
        return valtype
    raise MalformedModule(f"Invalid byte while parsing reftype.  Got '{valtype}")
