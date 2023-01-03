#sum of first (requested) natural numbers
import time
def add(num):
    if num < 1:
        return "Invalid number! Please enter number greater than or equal to 1"

    elif num == 1:
        return 1

    else:
        sum = num+add(num-1)
        return sum

while True:
    num = int(input("Sum of how many numbers: "))
    print(add(num))
    add(num)

    
