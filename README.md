# py-wasm

This is a fork of the original project that is no longer maintained: [ethereum/py-wasm](https://github.com/ethereum/py-wasm).
The specific purpose of this fork is to support the [wasm-semantics](https://github.com/runtimeverification/wasm-semantics) project. As of now, our primary focus is on the development and enhancement of the binary parser module to align with the latest WebAssembly standard updates.

## Developer Setup

You can set up your dev environment with:

```sh
virtualenv -p python3 venv
. venv/bin/activate
pip install -e .[dev]
```

Run binary parser tests with:

```sh
make test-binary-parser
```

### Testing Setup

During development, you might like to have tests run on every file save.

Show flake8 errors on file change:

```sh
# Test flake8
when-changed -v -s -r -1 wasm/ tests/ -c "clear; flake8 wasm tests && echo 'flake8 success' || echo 'error'"
```

Run multi-process tests in one command, but without color:

```sh
# in the project root:
pytest --numprocesses=4 --looponfail --maxfail=1
# the same thing, succinctly:
pytest -n 4 -f --maxfail=1
```

Run in one thread, with color and desktop notifications:

```sh
cd venv
ptw --onfail "notify-send -t 5000 'Test failure ⚠⚠⚠⚠⚠' 'python 3 test on py-wasm failed'" ../tests ../wasm
```

### Release setup

For Debian-like systems:
```
apt install pandoc
```

To release a new version:

```sh
make release bump=$$VERSION_PART_TO_BUMP$$
```

#### How to bumpversion

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, specify which part to bump,
like `make release bump=minor` or `make release bump=devnum`. This is typically done from the
master branch, except when releasing a beta (in which case the beta is released from master,
and the previous stable branch is released from said branch). To include changes made with each
release, update "docs/releases.rst" with the changes, and apply commit directly to master 
before release.

If you are in a beta version, `make release bump=stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the
new version explicitly, like `make release bump="--new-version 4.0.0-alpha.1 devnum"`


## Development and Testing

The test suite in this library is run using `pytest`.

```sh
pytest tests/
```

Part of the test suite includes the *spec* tests from the official Web Assembly
spec.  These are found under `./tests/spec`.

It is often useful to view logging output when running tests.  This can be done with:

```sh
pytest tests/spec/ --log-cli-level=debug
```

When trying to diagnose a specific failure in a spec test it can be useful to
run the tests in a branch that is currently passing, capture the logging
output, and then compare it to the logging output of the test in the failing
branch.  In order to make it easier to get the relevant logging output, you can
use the flag `--stop-after-command-line=123` where `123` is the line for the
failing command.  The full command would look something like:

```sh
pytest tests/spec/ --log-cli-level=debug --stop-after-command-line=123 -k f32.wast
```

This sets the logging output to `DEBUG` level, stops the test suite after it
passes command line `123` and only runs the spec tests from the `f32.wast` spec
test file.

There are a few spec tests that take noticeably longer than the others.  You
can omit these from the test run by adding the flag `--skip-slow-spec`.
