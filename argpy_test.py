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

import argpy


parser = argpy.OptionParser()
parser.accepts("test").with_required_arg()
option_set = parser.parse(args=["--test", "Hello", "--test=World"])
for option in option_set:
    print(option.get_parsed_arg())
