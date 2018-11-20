'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


import os

#initializing
list_of_paths = []

os.chdir('C:\\Dropbox\\0 Library')
files_md5 = {}

#making list of paths
for root, dirs, files in os.walk("."):
    print(root)
    #for filename in files:
       # full_path = 'C:\\Dropbox\\0 Library' + root[1:] + '/' + filename
        #list_of_paths.append(full_path)
#print(list_of_paths)

'''
#making dictionary of {(paths: md5)}
for file in list_of_paths[0:300]:
    cmd = 'md5sum ' + "'" + file + "'"
    fp = os.popen(cmd)
    res = fp.read()
    files_md5[file] = res[0:32]
    stat = fp.close()

#initializing
duplicates = {}
uniques = {}
md5s = []
files = []

#making list of md5 hash and corresponding list of files (with corresponding indexes)
for x in files_md5:
    md5s.append(files_md5[x])
    files.append(x)

#printing
print(md5s)
print('list of paths -' + str(len(list_of_paths)))
print('dict -' + str(len(files_md5)))

print('md5s -' + str(len(md5s)))
print('files -' + str(len(files)))

#making list of duplicates
counter = 0
duplicates = []             #initializing dup list
for _hash in md5s:
    for each in md5s:       #for loop withing for loop looping same list
        if _hash == each:
            counter += 1    #if it finds a duplicate it makes counter > 1
    if counter > 1:         #and if counter > 1 there is dup so adds to list
        if _hash not in duplicates:
            duplicates.append(_hash)
    counter = 0             # resetting counter after each
print('duplicates - ' + str(len(duplicates)))
print(duplicates)

# printing list of duplicates
for dup in duplicates:
    print(files[md5s.index(dup)])



'''
