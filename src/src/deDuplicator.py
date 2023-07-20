import os, filecmp

# the directory name
# dirname = '/home/user/Pictures'

# list of files in the directory
def deDuplicator(dirname):
    files = os.listdir(dirname)
    # print(files)

    # loop through the files only with the selected extention
    for file in files:
        file_path = os.path.join(dirname, file)
        file_size = os.stat(file_path).st_size
        ext = file.rsplit('.', 1)[1].lower()

        for comp_file in files:
            comp_ext = comp_file.rsplit('.',1)[1].lower()
            comp_file_path = os.path.join(dirname, comp_file)
            comp_file_size = os.stat(comp_file_path).st_size

            if comp_file != file and comp_ext == ext and comp_file_size == file_size:
                comp = filecmp.cmp(file_path, comp_file_path, shallow=False)

                if comp:
                    os.remove(comp_file_path)
                    files.remove(comp_file)
                    # print(files)

