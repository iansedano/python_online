fruit = 'banana'
letter = fruit[1]

print(letter)

index = 0

while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

index = len(fruit) - 1

while index > -1:
    letter = fruit[index]
    print(letter)
    index = index - 1

for letter in fruit:
    print(letter, end='')

print('\n')

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        p_letter = letter + 'u'
    else:
        p_letter = letter
    print(p_letter + suffix)

print('\n')

s = 'Monty Python'
print(s[0:5])
print(s[6:12]) #excludes last character

print(fruit[:4])
print(fruit[3:])
print(fruit[2:2])
print(fruit[:])

print('\n')

greeting = 'Hello, World!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find('Banana','n'))

def find_2(word, letter, position):
    index = position
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find_2('Banana','n',5))

print('\n')

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

def count(string, letter_to_find):
    counter = 0
    for letter in string:
        if letter == letter_to_find:
            counter = counter + 1
    return counter

print(count('banananana','n'))

def count_2(string, letter_to_find, position):
    counter = 0
    index = position
    while index < len(string):
        if string[index] == letter_to_find:
            counter += 1
        index += 1
    return counter

print(count_2('nanananananananana', 'a', 5))

print('\n')

word = 'banana'
new_word = word.upper()  #invoking upper on word
print(new_word)
index = word.find('a')
print(index)
index = word.find('na')
print(index)
index = word.find('na',3) #optional argument
print(index)
index = word.find('na',3,4)
print(index) #gives -1 because cannot find it

print('\n')

print('a' in 'banana')
print('seed' in 'banana')

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter, end ='')
in_both('hewnlulnow','fajsdolfijeh')

print('\n')

print('zealot' < 'applemaniasd')

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j > -1:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True
print(is_reverse('pots', 'stop'))
