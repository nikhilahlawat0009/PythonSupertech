# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will demo HOWTO repeat a BLOCK of
# commands a specific number of times using a COUNTER look.


"""
    Docstring
"""

count = 0 # Initialise counter
while count < 10: # Test condition
    print(count)
    count += 1 # Increment counter

# Alternatively we could use a for loop plus the
# builtin in range (start, stop, step) function

for num in range(0,100,5):
    print(num)
