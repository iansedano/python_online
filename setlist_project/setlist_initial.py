
import os


#sheet music location

path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)




#making list of paths

def list_files(extension):
    for root, dirs, files in os.walk("."):
        return [f for f in files if f.endswith('.' + extension)]

list_of_full_paths = list_files('txt')

print(list_of_full_paths)

'''
#making list of paths
list_of_full_paths = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_path = full_path_to_folder  + root[1:] + '\\' + filename
        list_of_full_paths.append(full_path)
'''
