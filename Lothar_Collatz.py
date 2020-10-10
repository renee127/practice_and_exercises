# Lothar Collatz c0 hypothesis.

# Prompt user to enter number
c0 = int(input("Enter a non-negative and non-zero integer: "))

# Initialize steps for process
steps = 0

# While loop to process c0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        steps += 1
        print(int(c0))
    else:
        c0 = 3 * c0 + 1
        steps += 1
        print(int(c0))

print("Steps = ", steps)