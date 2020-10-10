# Find the height of the pyramid.

# Prompt user to enter number
blocks = int(input("Enter the number of blocks: "))
height = 0
i = 1
# loop to find height (=base)
while blocks >= i:
    height = i
    blocks = blocks - i
    i = i + 1
print("The height of the pyramid:", height)
