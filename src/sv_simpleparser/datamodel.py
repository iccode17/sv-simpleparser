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

"""Data Model."""

from pathlib import Path
from typing import Literal

import pydantic as pyd


class _BaseModel(pyd.BaseModel):
    model_config = pyd.ConfigDict(frozen=True)


class Port(_BaseModel):
    """Represents a port in a SystemVerilog module.

    Attributes:
        direction: Port direction ('input', 'output', 'inout')
        ptype: Port type
        name: Name of the port
        width: Bus width specification (e.g., '[7:0]')
        comment: List of associated comments
    """

    direction: Literal["input", "output", "inout"]
    # TODO: reg/wire/logic and unsigned/signed are two different kinds of categories
    #       right?, should they be separated?
    ptype: Literal["reg", "wire", "logic", "unsigned", "signed"] | None
    name: str
    width: str | None = None
    comment: list[str] | None = None


class Param(_BaseModel):
    """Represents a parameter in a SystemVerilog module.

    Attributes:
        ptype: Parameter type ('integer', 'real', 'string', etc.)
        name: Name of the parameter
        width: Bus width specification if applicable
        comment: List of associated comments
    """

    ptype: str | None = None
    name: str
    width: str | None = None
    comment: list[str] | None = None


class Module(_BaseModel):
    """Represents a SystemVerilog module."""

    name: str
    params: tuple[Param, ...]
    ports: tuple[Port, ...]


class File(_BaseModel):
    """Represents a SystemVerilog File."""

    path: Path | None
    modules: tuple[Module, ...]
