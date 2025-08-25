import math

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))
print(math.pow(2,3))


import random

print(random.randint(1, 10))   # Random number between 1 and 10 (inclusive)
print(random.choice(["A","B","C"]))  # Randomly picks one element
print(random.random())         # Random float between 0 and 1


import datetime

print(datetime.date.today())         # 2025-08-17
print(datetime.datetime.now())       # 2025-08-17 12:34:56
print(datetime.date.today().year)    # 2025
print(datetime.date.today().month)   # 8
print(datetime.date.today().day)     # 17




# 1. Age calculation
birth_year = int(input("Enter your birth year: "))
current_year = datetime.date.today().year
age = current_year - birth_year
print("Your age is:", age)

# 2. Lucky number
lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

# 3. Prime check using math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(age):
    print("Your age is a prime number!")
else:
    print("Your age is not a prime number.")
