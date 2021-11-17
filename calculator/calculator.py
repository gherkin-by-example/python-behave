# This file is part of gerkin-by-example
#
# Copyright (C) 2021 Rafael Guterres Jeffman
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <https://www.gnu.org/licenses/>.

"""Implement the domain."""


class Calculator:
    """A helper for math novices."""

    def __init__(self):
        """Initialize calculator object."""
        self.numbers = []

    def add_input(self, value):
        """Add a new input to the calculator."""
        self.numbers.append(value)

    def sum(self):
        """Sum two numbers."""
        return self.numbers.pop() + self.numbers.pop()
