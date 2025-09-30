# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will demo HOWTO check which platform
# your program is running on
"""
    Docstring
"""

import sys
import os

if sys.platform == 'win32':
    my_home = os.environ['HOMEPATH']
elif sys.platform == 'darwin' or sys.platform == 'linux':
   my_home = os.environ['HOME']
else:
    print("Running on some other os")

print("Home is", my_home)
