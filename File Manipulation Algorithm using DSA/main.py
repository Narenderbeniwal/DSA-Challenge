import os
import shutil

## Code for sorting the files and creating the folder
path= input("Enter the location: - ")
names = os.listdir(path)
folder_name = ['image','text','python','video','pdf','ducument']
for x in range(0,6):
     if not os.path.exists(path+folder_name[x]):
           os.makedirs(path + folder_name[x])

for files in names:
    if ".png" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files, path+'image/'+files)
    if ".txt" in files and not os.path.exists(path+'text/'+files):
        shutil.move(path+files, path+'text/'+files)
    if ".ipynb" in files and not os.path.exists(path+'python/'+files):
        shutil.move(path+files, path+'python/'+files)
    if ".mp3" in files and not os.path.exists(path+'video/'+files):
        shutil.move(path+files, path+'video/'+files)
    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
        shutil.move(path+files, path+'pdf/'+files)
    if ".docx" in files and not os.path.exists(path+'ducument/'+files):
        shutil.move(path+files, path+'ducument/'+files)