#Created by: Felber Christoph "faelb"
#Programm nimmt Dateien vom PC von einem fixen Pfad
#und kopiert diese auf einen angeschlossenen USB Stick


#program start


# importing required modules
from zipfile import ZipFile
import os

# def getFilePath(directory):
#     filePaths = []
#
#     for root, directories, files in os.walk(directory):
#         for filename in files:
#             filepath = os.path.join(root, filename)
#             filePaths.append(filepath)
#
#     print("following files are in the path")
#     for filename in filePaths:
#         print(filename)


def main():

#os walk geht aufgrund von 3 eingaben einen Tree durch des jeweiligen directories
#os.walk() root: der angegebene path
#os.walk() dir: subdirectories im angegebenen path
#os.walk() files: all files from actual root
    basename = "C:\\Users\\faelb\\Desktop\\testfolderToUSB"
    filepaths = []

    for root, dir, files in os.walk("C:\\Users\\faelb\\Desktop\\testfolderToUSB"):
        for filenames in files:
            filepaths.append(os.path.join(root, filenames))
            print("all paths added")

    with ZipFile("C:\\Users\\faelb\\Desktop\\myZip.zip", 'w') as zip:
        for files in filepaths:
            zip.write(files, basename)

    print("Files zipped")
        #print("root: ", root)
        #print("dir: ", dir)
        #print("files: ", files)

    #getFilePath("C:/Users/faelb/Desktop/testfolderToUSB")

main()