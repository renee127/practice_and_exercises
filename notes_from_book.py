"""These are notes from/inspired by Python Crash Course.
"""
import this # zen of python


# f string formatting examples
print('')
first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print(f'Hello, {full_name.title()}!')
# old way to format 3.5 and earlier
full_name = '{} {}'.format(first_name, last_name)
print(full_name)
print('no tab')
print('\t with tab ')
print('\n new line but adds a space \n')
print('no space')
print('')
print('Sharks:\n\tHammerhead\n\tReef\n\tNursery')
print('          (before) removing whitespace    ' + '.')
white_space = '          removing whitespace    '
print(white_space.lstrip() + '.')
print(white_space.rstrip() + '.')
print(white_space.strip() + '.')
print('sometimes it helps to visualize large numbers')
print('python (3.6^) lets you group like so 27_000_000_027 = ')
print(27_000_000_027)
print('Use all caps for a constant: MAX_CATS = 3')
names = ['a', 'c', 'z', 'd', 'p']
names.reverse()
print(names) # notice it just flips, not alphabetical
names.reverse()
print('sort forgets intial order while sorted is temp')
print(names)
print(sorted(names))
print(names)
print(sorted(names, reverse=True))
print(names)
names.sort() # permanetly changes the order in names
print(names)
print(names)
names.sort(reverse = True)
print(names)
print(names) # stays reversed
print('A list comprehension puts everything on 1 line')
squares = [value**2 for value in range(1, 11)]
print(squares)
to_twenty = [num + 1 for num in range(0, 20)]
print(to_twenty)
cubes = [num * num for num in range(0, 20)]
print(cubes)
million = [num + 1 for num in range(0, 1000)]
print(max(million))
print(min(million))
print(sum(million))
threes = [num * 3 for num in range(1, 11)]
print(threes)
odds = [num for num in range(1, 20, 2)]
print(odds)
