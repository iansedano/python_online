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
os.chdir('C:/Dropbox/Cargas de cámara')
files_md5 = {}

#making list of paths
for root, dirs, files in os.walk("."):
    for filename in files:
        list_of_paths.append(filename)
print(list_of_paths)


#making dictionary of {(paths: md5)}
for file in list_of_paths:
    cmd = 'md5sum ' + file
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()

    print(res)
    print(stat)
