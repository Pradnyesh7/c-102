

import os
import shutil

from_dir = "C:/Users/sdsur/Downloads/pptx"           
to_dir = "C:/Users/sdsur/OneDrive/Desktop/whitehat.jr/projects/project-102/downloaded file"



list_of_files = os.listdir(from_dir)


for file in list_of_files:
    name, ext = os.path.splitext(file)

    
    ext = ext[1:]

   
    if ext == '':

        continue

      

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + key 
        path3 = to_dir + '/' + key + '/' + file_name

        if os.path.exists(path2):

            print("Directory Exists...")
            print("Moving " + file_name + "....")
            shutil.move(path1, path3)

        else:
            print("Making Directory...")
            os.makedirs(path2)
            print("Moving " + file_name + "....")
            shutil.move(path1, path3)
                   
