# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will simulate a high street bank atm machine
"""
    Docstring
"""

master_pin = "023"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
        attempts += 1

else:
    # only execute once if while loop becomes false!
    print("Too many attempts")
    print("Your card has been retained, have a nice day")




print("Done")