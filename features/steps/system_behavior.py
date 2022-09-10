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

"""Steps implementation for system level."""


import subprocess

from behave import given, then, when  # pylint: disable=no-name-in-module


@given("the input is")
def _given_input(context):
    context.stdin_data = context.text


@when('the program "{program}" runs')
def _when_program_runs(context, program):
    context.result = subprocess.run(
        ["python", "-m", program],
        capture_output=True,
        check=True,
        text=True,
        input=context.stdin_data,
    )


@then("the output should be")
def _then_output_should_be(context):
    # Python's bytes.splitlines use the 'universal newlines' approach
    # so that specific line break characters are not relevant, but a
    # line break is.
    expected = context.text.splitlines()
    observed = context.result.stdout.splitlines()
    assert expected == observed
