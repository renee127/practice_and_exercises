"""
    Determine if a string is a palindrome.
"""

# TODO: get input and initialize lists of input and reverse
word = input('Type the string to check if it is'
    ' a palindrome: ')
test_word = list(word)
rev_word = list(reversed(test_word))
statement = ', is a palindrome.'

# TODO: loop to check each letter
for i in range(len(test_word)):
    if test_word[i] == rev_word[i]:
        i += 1
    else:
        statement = ', is not a palindrome.'
print('The word, ' + word + statement)

