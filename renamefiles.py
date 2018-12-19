import os


def rename_files():

    # (1) get file names from folder
    filelist = os.listdir(r"C:\Users\diogo.sousa\Documents\Estudos\FullStack\prank")
    print (filelist)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\diogo.sousa\Documents\Estudos\FullStack\prank")
    for file in filelist:
        print("Old name: "+file+" ---> New name: "+file.translate(None, "0123456789"))
        os.rename(file, file.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()

def renameunexist():
    filelist = os.listdir(r"C:\Users\diogo.sousa\Documents\Estudos\FullStack\prank\teste")
    print(filelist)
    os.chdir(r"C:\Users\diogo.sousa\Documents\Estudos\FullStack\prank\teste")
    for file in filelist:
            os.rename(file,'sydney.jpg')
            print(file)

renameunexist()

os.rename('arquivo','novo')
