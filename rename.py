from PIL import Image
import os, sys

path = "../FakeImageDetection/train/"
dirs = os.listdir( path )
               
def rename():

    for item in dirs:
        i = 0
        for filename in os.listdir(path + item):
            im = Image.open(path + item + '/' + filename)
            file, ext = os.path.splitext(path + item + '/' + filename)
            #print(file,ext)
            im.close()
            dst ="picture" + str(i) + ext
            src =path+item+'/'+ filename
            dst =path+item +'/'+ dst
            os.replace(src, dst)
            i += 1
#rename()
