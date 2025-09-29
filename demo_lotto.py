# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: This script will generate unique random lottery numbers

"""
    Docstring:

"""
import random

lotto =[] #Create empty list



while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)

    else:
        print("Duplicate number =", num)


print("Lottery numbers = ", lotto)




