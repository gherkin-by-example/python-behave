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

"""Steps implementation for domain level feature."""


from behave import given, when  # pylint: disable=no-name-in-module


@given("the first number is {number:d}")
def _given_first_number(context, number):
    context.calculator.add_input(number)


@given("the second number is {number:d}")
def _given_second_number(context, number):
    context.calculator.add_input(number)


@when("the two numbers are added")
def _when_two_numbers_are_added(context):
    context.result = context.calculator.sum()
