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
"""Command Line Interface."""

from pathlib import Path

import click

from ._gen_templates import gen_instance, gen_markdown_table
from ._sv_parser import parse_sv


@click.group()
def cli():
    """Easy-To-Use SystemVerilog Parser."""
    pass


arg_filepath = click.argument("file_path", type=click.Path(exists=True, readable=True, path_type=Path))


@cli.command()
@arg_filepath
def gen_sv_instance(file_path: Path):
    """Parses an SystemVerilog file and returns a instance of the module."""
    mod_lst = parse_sv(file_path)

    for mod_obj in mod_lst:
        instance = gen_instance(mod_obj)
        print(instance)


@cli.command()
@arg_filepath
def gen_io_table(file_path: Path):
    """Generates an I/O table from an SV file."""
    mod_lst = parse_sv(file_path)

    for mod_obj in mod_lst:
        table = gen_markdown_table(mod_obj)
        print(table)


@cli.command()
@arg_filepath
def print_tokens(file_path: Path):
    """Print tokens for debug."""
    parse_sv(file_path)
