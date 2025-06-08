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

from dataclasses import dataclass


@dataclass
class Port:
    """Represents a port in a SystemVerilog module.

    Attributes:
        direction: Port direction ('input', 'output', 'inout')
        ptype: Port type ('wire', 'reg', 'logic', etc.)
        name: Name of the port
        width: Bus width specification (e.g., '[7:0]')
        comment: List of associated comments
    """

    direction: str
    ptype: str | None = None
    name: str | None = None
    width: str | None = None
    comment: list[str] | None = None


@dataclass
class Param:
    """Represents a parameter in a SystemVerilog module.

    Attributes:
        ptype: Parameter type ('integer', 'real', 'string', etc.)
        name: Name of the parameter
        width: Bus width specification if applicable
        comment: List of associated comments
    """

    ptype: str | None = None
    name: str | None = None
    width: str | None = None
    comment: list[str] | None = None
