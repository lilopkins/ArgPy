# ArgPy, a command line argument parser
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys


class Option:
    hasArgument = 0 # 0 - no, 1 - optional, 2 - required
    parsedArg = None

    def __init__(self, name):
        self.name = name

    def with_required_arg(self):
        self.hasArgument = 2
        return self

    def with_optional_arg(self):
        self.hasArgument = 1
        return self

    def get_parsed_arg(self):
        return self.parsedArg

    def set_parsed_arg(self, arg):
        self.parsedArg = arg
        return self

    def get_identifier(self):
        return "--%s" % self.name

    def __str__(self):
        return self.name


class OptionParser:
    options = []

    def accepts(self, name):
        opt = Option(name)
        self.options.append(opt)
        return opt

    def parse(self, args=sys.argv):
        parsed_arguments = []
        expects_param = False
        current_argument = None
        for argument in args:
            for argPart in argument.split("="):
                if argPart.startswith("--"):
                    if expects_param and current_argument.hasArgument == 2:
                        print("%s required a parameter!" % current_argument.get_identifier())
                        exit(1)
                    expects_param = False
                    for possibleArgument in self.options:
                        if possibleArgument.get_identifier() == argPart:
                            current_argument = possibleArgument
                            break
                    if current_argument is not None and current_argument.hasArgument > 0:
                        expects_param = True
                elif expects_param:
                    current_argument.set_parsed_arg(argPart)
                    expects_param = False
                    parsed_arguments.append(current_argument)
                    current_argument = None
                else:
                    print("Unrecognised: %s" % argPart)
        if expects_param and current_argument.hasArgument == 2:
            print("%s required a parameter!" % current_argument.get_identifier())
            exit(1)
        return parsed_arguments
