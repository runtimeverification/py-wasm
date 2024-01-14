import sys
from io import BytesIO
from pathlib import Path
from subprocess import run

import pytest

from wasm.parsers import parse_module

BINARY_DIR = Path(__file__).parent / 'data'
BINARY_WAT_FILES = BINARY_DIR.glob('*.wat')

sys.setrecursionlimit(100000)


@pytest.mark.parametrize('wat_path', BINARY_WAT_FILES, ids=str)
def test_binary_parser(wat_path: Path) -> None:
    # Given
    wat2wasm_cmd = ['wat2wasm', str(wat_path), '--output=/dev/stdout']
    proc_res = run(wat2wasm_cmd, check=True, capture_output=True)
    wasm_file = BytesIO(proc_res.stdout)

    assert not proc_res.returncode

    # Then
    parse_module(wasm_file)
