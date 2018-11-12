'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

print('type something')
my_string = input()
print(my_string.upper())
print(my_string.lower())


def is_vowel(letter):
    vowels = 'aeiou'
    i = 0
    while i < len(vowels):
        if letter == vowels[i]:
            return True
        i += 1
    return False

j = 0
while j < len(my_string):
    if is_vowel(my_string[j]):
        print(my_string[j].lower(), end = '')
    else:
        print(my_string[j].upper(), end = '')
    j += 1








