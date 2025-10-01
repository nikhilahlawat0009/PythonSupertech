# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will demo how to define name and
# call a use function with optional parameters,
# default values and optional return values.

"""
    Docstring
"""

def say_hello(greeting:str = "Namaste", recipient:str = "doston")->None:

    message =f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends")
say_hello("Hello", "chore")
say_hello("hello", "ishi")
say_hello()
say_hello("hello", "42")
