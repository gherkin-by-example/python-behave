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

Feature: URI1001 CLI

Narrative:

In order to avoid silly mistakes
As a math novice
I want to be told the sum of two numbers

Scenario: Run program with 10 and 9 (pos,pos)

Given the input is
"""
10
9
"""
When the program "calculator" runs
Then the output should be
"""
X = 19

"""

Scenario: Run program with -10 and 4 (neg,pos)

Given the input is
"""
-10
4
"""
When the program "calculator" runs
Then the output should be
"""
X = -6

"""

Scenario: Run program with 15 and -7 (pos,neg)

Given the input is
"""
15
-7
"""
When the program "calculator" runs
Then the output should be
"""
X = 8

"""
