import io
from typing import (
    Tuple,
)

from wasm import (
    constants,
)
from wasm.exceptions import (
    ParseError,
)
from wasm.typing import (
    UInt8,
)

from .byte import (
    parse_single_byte,
)

KNOWN_VERSIONS = {
    constants.VERSION_1,
}


def parse_version(stream: io.BytesIO) -> Tuple[UInt8, UInt8, UInt8, UInt8]:
    """
    https://webassembly.github.io/spec/core/bikeshed/index.html#binary-version
    """
    actual = (
        parse_single_byte(stream),
        parse_single_byte(stream),
        parse_single_byte(stream),
        parse_single_byte(stream),
    )
    if actual not in KNOWN_VERSIONS:
        raise ParseError(
            f"Unknown version. Got: "
            f"{tuple(hex(byte) for byte in actual)}"
        )
    return actual
