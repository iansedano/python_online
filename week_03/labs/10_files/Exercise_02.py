'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.

Solution: http://thinkpython2.com/code/sed.py.

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html
'''


'''
string1 = """Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”

    Ah, distinctly I remember it was in the bleak December;
And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;—vainly I had sought to borrow
    From my books surcease of sorrow—sorrow for the lost Lenore—
For the rare and radiant maiden whom the angels name Lenore—
            Nameless here for evermore."""
string2 = ''

def rep_string(pat, rep, string):
    pos = 0
    list_pos = []
    while string.find(pat,pos) != -1:
        start = string.find(pat,pos)
        end = string.find(pat,pos) + len(pat)
        list_pos.append((start, end))
        pos = end
    print(list_pos)

rep_string('more', 'xxxxx', string1)

'''

def sed(pat, rep, path1, path2):

    # initial definitions
    pos = 0
    list_pos = []

    file1 = open(path1, 'r', encoding="utf8")
    file2 = open(path2, 'w')

    file_string = file1.read()


    # making list of positions of the target pattern
    while file_string.find(pat,pos) != -1:

        start = file_string.find(pat,pos)
        end = start + len(pat)

        list_pos.append(start)
        pos = end
    print(list_pos)


    #writing the string
    string_to_write = '' #string to be
    tracker = 0

    for target in list_pos:
        string_to_write = string_to_write + file_string[tracker:target] + rep
        tracker = target + len(pat)
        print(tracker, end=' ')

    # writing the last part of the string

    string_to_write = string_to_write + file_string[tracker:]
    file2.write(string_to_write)

    # FIN
    file1.close()
    file2.close()

sed('Raven', '____RAVEN____', 'the_raven.txt', 'the_raven_mod.txt')


