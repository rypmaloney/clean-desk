from os import listdir
import shutil
import glob

desktop_path = '/Users/productmanager/desktop/'
pdf_dir = '/Users/productmanager/desktop/PDF'
images_dir = '/Users/productmanager/desktop/images'
dir = listdir(desktop_path)
png = glob.glob(desktop_path + '*.png')
pdf = glob.glob(desktop_path + '*.pdf')


for f in pdf:
    shutil.move(f, pdf_dir)
