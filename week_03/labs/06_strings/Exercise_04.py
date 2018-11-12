'''
Write a script that finds the first vowel in a a user inputted string.

'''

string = 'qwerty'

vowels = 'aeiou'

def find_vowel(word):
    i = 0
    j = 0
    while i < len(word):
        j = 0
        while j < len(vowels):
            if word[i] == vowels[j]:
                return i
            j += 1
        i += 1


print(find_vowel(string))

