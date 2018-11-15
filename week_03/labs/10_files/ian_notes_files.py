fout = open('output.txt', 'w')

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of out land.\n"
fout.write(line2)

x = 52

fout.write(str(x))
fout.close()

camels = 42
print('%d' % camels) #prints string

print('I have spotted %d camels.' % camels)

print('in %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

# print('%d %d %d' % (1,2)) gives error idem for format mismatch



#/// EXCEPTIONS
print('\n\n/////EXCEPTIONS/////\n')

try:
    fin = open('bad_file')
except:
    print('something went wrong')


#/// DATABASES
print('\n\n/////DATABASES/////\n')

import dbm

db = dbm.open('captions', 'c')

db['cleese.png'] = 'Photo of John Cleese.'

print(db['cleese.png']) #output begins with b because its a bytes object

#some methods, like keys and items dont work with dbs

for key in db:
    print(key, db[key])

db.close()

#/// PICKLE
print('\n\n/////PICKLE/////\n')

import pickle #for storing anything that is not a string/byte in a database

t = [1,2,3]
print(pickle.dumps(t))
s = pickle.dumps(t)
t2 = pickle.loads(s)
print(t2)

print()

import os

cmd = 'dir'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(fp)
print(res)
print(stat)

#  FOLLOWING CODE MUST BE RUN IN UNIX ENVIRONMENT

open("md5.txt" , 'w')
to_chk_md5 = "md5.txt"
cmd = 'md5sum ' + to_chk_md5
print(cmd)
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)


#/// WRITING MODULES
print('\n\n/////WRITING MODULES/////\n')


import wc

print(wc)

print(__name__)

print(wc.linecount('ian_notes_files.py'))


#/// DEBUGGING
print('\n\n/////DEBUGGING/////\n')

#finding whitespaces for debugging

s = '1 2\t 3\n 4'
print(s)
print(repr(s))
