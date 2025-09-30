# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: Split and rejoin strings

"""
    Docstring
"""

# Sample line from /etc/passwd in linux for the root user account
line = "root:x:0:0: The Super User:/root:/bin/bash"

# want to modify stings ut they are immutable

fields = line.split(":")
fields[4] = "The Administrator"
fields [6] = "/bin/zsh"

":".join(fields) # returns a new string

print(fields)

print("modified str =", line)

