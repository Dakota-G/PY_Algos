from math import sqrt
# These are algorithms based in mathematical functions

#  Factorials. A number factorial is that number multiplied by all numbers that come before it
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# find the fibonacci number at the place given in the argument
def fibonacci(end):
    if end < 0:
        return("Error")
    if end == 1:
        return 0
    elif end == 2:
        return 1
    else:
        return fibonacci(end - 1) + fibonacci(end - 2)

def pythagorean():
    side = str(input("Which side are we finding?").lower())

    if side == 'a':
        try:
            b = int(input("What is the length of side b?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        try:
            c = int(input("What is the length of side c?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        side = sqrt((c * c) - (b * b))
        return side
    elif side == 'b':
        try:
            a = int(input("What is the length of side a?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        try:
            c = int(input("What is the legnth of side c?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        side = sqrt((c * c) - (a * a))
        return side
    elif side == 'c':
        try:
            a = int(input("What is the length of side a?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        try:
            b = int(input("What is the length of side b?"))
        except:
            input("Please input an integer! Press any key to retry.")
            return pythagorean()
        side = (a * a) + (b * b) 
        return side
    else:
        print("You must input a letter of 'a', 'b', or 'c'.")
        return pythagorean()

def findPrimes(limit):
    # creates list called primes where every entry is True
    primes = [True] * limit
    # go through the list and yield any index that is True
    for i in range(2, limit):
        if primes[i]:
            yield i
            # change to False any multiple of the number(cannot be Prime)
            for n in range(i*i, limit, i):
                primes[n] = False

def findPrimesTwo(limit):
    primes = []
    not_primes = []
    i = 2
    while len(primes) <= limit:
        if i not in not_primes:
            primes.append(i)
            n = i
            for _ in range(limit*2):
                n = n + i
                if n not in not_primes:
                    not_primes.append(n)
        i += 1
    return not_primes

print(findPrimesTwo(100))
