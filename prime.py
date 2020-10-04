# Takes a number as input and 
# returns the prime numbers 

number = int(input('Please enter a number: '))

factors = list()
factor = 2
# Create a loop to factorize number
while factor <= number:
    if number % factor == 0:
        number = int(number / factor)
        print(number)
        factors.append(factor)
    else:
        factor += 1
print(factors)


