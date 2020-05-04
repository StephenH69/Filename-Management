import os, shutil, pathlib
import myconfig as mc
from zipfile import ZipFile

if mc.base_dir == "":
    base_dir = pathlib.Path().absolute()
else:
    base_dir = mc.base_dir

# RENAME FILES
if mc.selection == 1:
    path = base_dir + "/" + mc.orig_dir
    for f in os.listdir(path):
        os.rename(os.path.join(path, f), os.path.join(path, f.replace(mc.old_file, mc.new_file)))

# RENAME DIRECTORY
if mc.selection == 2:
    directory_list = list()
    for root, dirs, files in os.walk(base_dir, topdown=False):
        for name in dirs:
            os.rename(os.path.join(base_dir, name), os.path.join(base_dir, name.replace(mc.orig_dir, mc.new_dir)))

# COPY FOLDER
if mc.selection == 3:
    origin_dir = base_dir + "/" + mc.orig_dir
    copy_dir = origin_dir + "_" + mc.new_dir
    shutil.copytree(origin_dir, copy_dir)

# ZIP FOLDER
if mc.selection == 4:
    zipFileName = mc.orig_dir + ".zip"
    print(base_dir)

    with ZipFile(zipFileName, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(mc.orig_dir):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath)
       