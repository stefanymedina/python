# number is odd
from random import randint
num = randint(1, 1000)
print(f"the number {num} is")

if num%2 != 0 :
    print("odd")
else:
    print("even")   