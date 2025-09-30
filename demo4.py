# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: Demo iterator loop

"""
    Docstring
"""
import sys
heroes =['Diana', 'Pele', 'SRA', 'Bhagat Singh']

# Iterate through the collection list using an iterator for loop

for name in heroes:
    print(name)


# Iterate thorugh list and modify the objects using an ITERATOR formloop and an index

idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes= ", heroes)


# Using an iterator for loop and built in enumerate() function
for (idx, name) in enumerate(heroes, start=0):
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes= ", heroes)

try:
    sys.exit("0") # Explicit EXIT with return code 90=success, 1-255=error code
except SystemExit:
    print("Goodbye")