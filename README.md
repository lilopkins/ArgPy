# ArgPy
A command line argument parser for Python, inspired by JOptSimple.

## Usage
To include this in a project, import the file:
```py
import argpy
```
To make use of the functionality of ArgPy, first create an `OptionParser`
```py
parser = argpy.OptionParser()
```
Then create acceptable `Option`s
```py
parser.accepts("foo").with_required_arg() # required argument
parser.accepts("bar").with_optional_arg() # optional argument
parser.accepts("foobar")                  # no argument
```
Then, parse the command line arguments, receiving an `OptionSet`
```py
option_set = parser.parse() # an optional parameter can be used to override the default use of sys.argv
```
Use the parsed `Option`s as desired:
```py
for option in option_set:
    print(option.get_parsed_arg()) # prints out any arguments parsed
```
