# MIT License
#
# Copyright (c) 2025 ericsmacedo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Test Command Line Interface."""

from pathlib import Path

from click.testing import CliRunner
from pytest import mark
from test2ref import assert_refdata

from sv_simpleparser.cli import cli

from .conftest import EXAMPLES_PATH

# We are just testing a reduced set of examples here
EXAMPLES = (
    EXAMPLES_PATH / "param_module.sv",
    EXAMPLES_PATH / "adder.sv",
    EXAMPLES_PATH / "bcd_adder.sv",
)


@mark.parametrize("example", EXAMPLES)
def test_gen_sv_instance(tmp_path, runner, example):
    """Test Info Command."""
    with runner.isolated_filesystem():
        # Run the command
        result = runner.invoke(cli, ["gen-sv-instance", str(example)])

        assert result.exit_code == 0
        (tmp_path / "output.txt").write_text(result.output)

    assert_refdata(test_gen_sv_instance, tmp_path, flavor=example.name)


@mark.parametrize("example", EXAMPLES)
@mark.parametrize("options", ((), ("--no-color",)))
def test_info(tmp_path, runner, example, options):
    """Test Info Command."""
    with runner.isolated_filesystem():
        # Run the command
        result = runner.invoke(cli, [*options, "info", str(example)])

        assert result.exit_code == 0
        (tmp_path / "output.md").write_text(result.output)

    assert_refdata(test_info, tmp_path, flavor=example.name)


@mark.parametrize("example", EXAMPLES)
def test_json(tmp_path, runner, example):
    """Test json Command."""
    with runner.isolated_filesystem():
        # Run the command
        result = runner.invoke(cli, ["json", str(example)])

        assert result.exit_code == 0
        (tmp_path / "output.json").write_text(result.output)

    assert_refdata(test_json, tmp_path, flavor=example.name)


def test_cli_help_smoke():
    """Test that help command works."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_empty(runner):
    """Test Empty File Command."""
    with runner.isolated_filesystem():
        empty_file = Path("file.sv")
        empty_file.touch()

        # Run the command
        result = runner.invoke(cli, ["info", str(empty_file)])

        assert result.exit_code == 1
