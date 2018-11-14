'''
Write a script that takes a sentence from the user and returns:

    - the number of lower case letters
    - the number of uppercase letters
    - the number of punctuations characters
    - the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
I love to work with dictionaries!
Example output:
Upper case: 1
Lower case: 26
Punctuation: 1

'''

my_string = 'I love to work with dictionaries!'
punctu = '!.,?;:"'

my_dict = {'lower':0,'upper':0,'punc':0, 'space':0}

for c in my_string:
    if c == ' ':
        my_dict['space'] += 1
    elif c in punctu:
        my_dict['punc'] += 1
    elif c == c.upper():
        my_dict['upper'] += 1
    elif c == c.lower():
        my_dict['lower'] += 1


print(my_dict)
