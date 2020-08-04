# Different ways to reverse arrays

n = 7 # num of elements in array
arr = [1, 7, 4, 5, 9, 2, 8]

import _sys

reversed_array = []
for i in range(n):
    reversed_array.append(arr[n-i-1])

output_string = ''
for i in range(len(reversed_array)):
    output_string += str(reversed_array[i]) + ' '
print(output_string)
# or use join method to join elements into list to replace 4 lines above
print(' '.join(str(i) for i in reversed_array))

# Or ... use python method reverse
    # reverse the order of the array
    reverse_arr = arr[::-1]

# loop to print each letter with space between
for i in range(n):
    print(reverse_arr[i], end = " ")
    i += 1


