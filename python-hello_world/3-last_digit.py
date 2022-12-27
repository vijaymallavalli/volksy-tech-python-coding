#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
n = number % 10
if number < 0:
    n = n - 10
if n == 0:
    print('last digit of',number,'is',n,'and is 0')
else:
    if n > 5:
         print('last digit of',number,'is',n,'and is greater than 5'
    else:
        print('last digit of',number,'is',n,'and is less than 6 and not 0')      
