from typing import (
    NamedTuple,
    Optional,
)

import numpy

from wasm import (
    constants,
)
from wasm._utils.numpy import (
    no_overflow,
)
from wasm.exceptions import (
    Trap,
    ValidationError,
)


class MemoryType(NamedTuple):
    """
    https://webassembly.github.io/spec/core/bikeshed/index.html#memory-types%E2%91%A0
    """
    min: numpy.uint32
    max: Optional[numpy.uint32]


class Memory(NamedTuple):
    type: MemoryType


class MemoryInstance:
    data: bytearray
    max: Optional[numpy.uint32]
    _length_cache: int

    def __init__(self, data: bytearray, max: numpy.uint32 | None = None) -> None:
        self.data = data
        self.max = max
        self._length_cache = len(self.data)

    @property
    def num_pages(self) -> numpy.uint32:
        return numpy.uint32(len(self.data) // constants.PAGE_SIZE_64K)

    def read(self, location: numpy.uint32, size: numpy.uint32) -> memoryview:
        with no_overflow():
            try:
                end_location = location + size
            except FloatingPointError:
                raise Trap(
                    f"Attempt to read from out of bounds memory location: {int(location) + size} "
                    f"> {len(self.data)}"
                )

        if end_location > self._length_cache:
            raise Trap(
                f"Attempt to read from out of bounds memory location: {end_location} "
                f"> {len(self.data)}"
            )
        return memoryview(self.data)[location:end_location]

    def write(self, location: numpy.uint32, value: bytes) -> None:
        end_index = location + len(value)
        if end_index > self._length_cache:
            raise Trap(
                f"Attempt to write to out of bounds memory location: "
                f"{end_index} "
                f"> {len(self.data)}"
            )
        self.data[location: end_index] = value

    def grow(self, num_pages: numpy.uint32) -> numpy.uint32:
        new_num_pages = num_pages + len(self.data) // constants.PAGE_SIZE_64K
        if new_num_pages >= constants.UINT16_CEIL:
            raise ValidationError(
                f"Memory length exceeds u16 bounds: {new_num_pages} > {constants.UINT16_CEIL}"
            )
        elif self.max is not None and self.max < new_num_pages:
            raise ValidationError(
                f"Memory length exceeds maximum memory size bounds: {new_num_pages} > "
                f"{self.max}"
            )

        self.data.extend(bytearray(num_pages * constants.PAGE_SIZE_64K))
        self._length_cache = len(self.data)
        return numpy.uint32(new_num_pages)
