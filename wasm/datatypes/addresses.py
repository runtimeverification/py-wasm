from typing import (
    Iterable,
    Tuple,
    Union,
)

TAddress = Union[
    'FunctionAddress',
    'ExternAddress',
    'GlobalAddress',
    'MemoryAddress',
    'TableAddress',
]


class FunctionAddress(int):
    @staticmethod
    def filter(values: Iterable[TAddress]) -> Tuple['FunctionAddress', ...]:
        return tuple(address for address in values if isinstance(address, FunctionAddress))


class ExternAddress(int):
    @staticmethod
    def filter(values: Iterable[TAddress]) -> Tuple['ExternAddress', ...]:
        return tuple(address for address in values if isinstance(address, ExternAddress))


class TableAddress(int):
    @staticmethod
    def filter(values: Iterable[TAddress]) -> Tuple['TableAddress', ...]:
        return tuple(address for address in values if isinstance(address, TableAddress))


class MemoryAddress(int):
    @staticmethod
    def filter(values: Iterable[TAddress]) -> Tuple['MemoryAddress', ...]:
        return tuple(address for address in values if isinstance(address, MemoryAddress))


class GlobalAddress(int):
    @staticmethod
    def filter(values: Iterable[TAddress]) -> Tuple['GlobalAddress', ...]:
        return tuple(address for address in values if isinstance(address, GlobalAddress))
