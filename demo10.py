# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will do some demo on user functions



#variable

def search_word(pattern=r"sage", *files):
    lines_matched = 0
    for file in files:

        with (open(file, mode="rt") as fh_in):
            for (line_num, line) in enumerate(fh_in, start=1):
                if line.isascii() and pattern in line:
                    print(line_num, line, end="")
                    lines_matched +=1
        return lines_matched


total_lines = 0
total_lines += search_word("arash", r"/Users/nan707/Documents/PythonPrograms/words")

print(f"Total lines matched '{total_lines}' lines")

