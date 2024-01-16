from typing import IO

from wasm.datatypes import (
    RefType,
    ValType,
)
from wasm.datatypes.addresses import ExternAddress, FunctionAddress
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

def parse_reftype(stream) -> RefType:
    valtype = parse_valtype(stream)
    if valtype is ValType.funcref:
        return FunctionAddress
    if valtype is ValType.externref:
        return ExternAddress
    raise MalformedModule(f"Invalid byte while parsing reftype.  Got '{valtype}")
