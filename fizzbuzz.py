"""For 1 - 100, program prints text or number per rules."""

for n in range(1, 101, 1):

    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
