# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will demo HOWTO create, and grow and shrink
# and combine sets (Unordered collection with unique values)

"""
    Docstring
"""


marvel_fans = {'ayo', 'charles', 'arash', 'zubin', 'diren', 'sage', 'donald'}

dc_fans = set()  # Crate an empty SET

# Grow a set

dc_fans.add('donald')
dc_fans.add('charles')
dc_fans.add('jason')

print(f"Fans of DC = {dc_fans}")



# Shrink a set

dc_fans.pop()

print(f"Fans of DC = {dc_fans}")
print(f"Fans of marvel = {marvel_fans}")

print(f"Fans of marvel or dc = {marvel_fans.union(dc_fans)}")

print(f"Fans of marvel and dc = {marvel_fans.intersection(dc_fans)}")

print(f"Fans of only DC = {dc_fans.difference(marvel_fans)}")
