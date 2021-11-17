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

@domain
Feature: Calculator

Narrative:

In order to avoid silly mistakes
As a math novice
I want to be told the sum of two numbers

Scenario Outline: Add two numbers

Given the first number is <a>
And the second number is <b>
When the two numbers are added
Then the result should be <x>

Examples:
|  a |  b |  x |
| 10 |  9 | 19 |
|-10 |  4 | -6 |
| 15 | -7 |  8 |
