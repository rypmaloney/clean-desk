
from gettext import find
import os
import shutil
import sys

# Use script with directory to be cleaned as an argument eg. python clean_desk.py /Users/ryanmaloney/desktop/   

dir_path = str(sys.argv[1])

locations = {
    'images': ['png', 'jpg', 'jpeg', 'gif' ],
    'sheets': ['csv', 'xls'],
    'notes': ['txt'],
    'docs': ['pdf', 'docx']
}

def get_extension(filename):
    return filename.rsplit('.', 1)[1]

def find_location(ext):
    key = [k for k,v in locations.items() if ext in v]  
    return next(iter(key or []), None)

def move_files(dir):
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)

        if file[0] != '.':
            #ignore hidden files like .env or .DS_Store
            if os.path.isfile(full_path):
                print(file)
                ext = get_extension(file)
                #check if file or directory
                if '.' in file:
                    #check if this is a standard filetype
                    desired_folder = find_location(ext)

                    if desired_folder:
                        #if folder doesn't exist, make it and add to desired folder
                        if os.path.isdir(dir + desired_folder) == False:
                            os.mkdir(dir + desired_folder)
                        shutil.move(full_path, dir + desired_folder)
                    else:
                        #create a new folder for this filetype
                        os.mkdir(dir + ext)
                        locations[ext] = ext
                        shutil.move(full_path, dir + ext)
                
if __name__ == '__main__':
    move_files(dir_path)
