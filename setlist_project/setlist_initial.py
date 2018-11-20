
import os


#sheet music location

path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)



#making list of paths

print(os.getcwd())

for root, dirs, files in os.walk("."):
    os.chdir(root)
    print('folder :' + root)
    for root, dirs, files in os.walk("."):
        print('files :')
        print(files)
    #for _dir in root:
    #    print(full_path_to_folder + '\\' + _dir)
        #return [f for f in files if f.endswith('.' + extension)]


"help - the beatles [open_mic solo_acoustic].txt"
#read the file into new file, then delete old file.

#list_of_full_paths = list_files('txt')

#print(list_of_full_paths)



'''
#making list of paths
list_of_full_paths = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_path = full_path_to_folder  + root[1:] + '\\' + filename
        list_of_full_paths.append(full_path)
'''
