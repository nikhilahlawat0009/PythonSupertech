# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: Practise, file handling

"""
    Docstring
"""
def isValid(line):
    if line.startswith('y') and line.endswith('n') and 'town' in line:
        return True
    return False


def main():
    with open('/Users/nan707/Documents/PythonPrograms/words', 'r') as f:
        count = 0
        for line in f:
            count+=1
            line_lower =line.lower().strip()
            if isValid(line_lower):
                lineUpper = line_lower.upper()
                final_string = f"{count}: {lineUpper}"
                print(final_string)

main()

