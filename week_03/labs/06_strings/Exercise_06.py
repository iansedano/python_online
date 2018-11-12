'''
Complete exercises in section 8.7 (p.75)

CODE:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

1) - Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.

2) - Rewrite this function so that instead of traversing the string,
it uses the three-parameter version of find from the previous section.

'''

def count(word,letter):
    count = 0
    for letter in word:
        if letter == 'letter':
            count = count + 1
    print(count)

def countx(word,letter):
    pos = 0
    count = 0
    while pos < len(word):
        pos = word.find(letter,pos)
        count += 1
        print(count)

print(countx('wawa','w'))



