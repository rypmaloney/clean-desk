from distutils.command.build_scripts import first_line_re
from gettext import find, gettext
import os
import shutil
import glob

desktop_path = '/Users/productmanager/desktop/'
dir = os.listdir(desktop_path)

locations = {
    'images': ['png', 'jpg', 'jpeg', 'gif' ],
    'sheets': ['csv', 'xls'],
    'notes': ['txt'],
    'docs': ['pdf', 'docx']
}


png = glob.glob(desktop_path + '*.png')
pdf = glob.glob(desktop_path + '*.pdf')

def get_extension(filename):
    return filename.rsplit('.', 1)[1]

def find_location(ext):
    '''Find the desired location based on file type and extension'''
    key = [k for k,v in locations.items() if ext in v]
    return key

def move_files():
    for file in os.listdir(desktop_path):
        full_path = os.path.join(desktop_path, file)

        if os.path.isfile(full_path):
            #check if file or directory
             if '.' in file:
                #check if this is a standard filetype
                desired_folder = find_location(get_extension(file))
                if len(desired_folder) > 0:
                    #check if this file is listed in locations
                    shutil.move(full_path, desktop_path + desired_folder[0])




if __name__ == '__main__':
    move_files()