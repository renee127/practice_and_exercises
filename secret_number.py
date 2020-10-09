secret_number = 777

print(
"""
+================================+
| Welcome to the game!           |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number:
    # check if the number matches secret number
    if number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        # read the next number
        number = int(input("Enter a number or type 0 to stop: "))
    else:
        # print the escape message
        number = 0
        print('"Well done, muggle! You are free now."')