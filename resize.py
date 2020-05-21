from PIL import Image
import os, sys
import cv2
from glob import glob

#path of files
path = "../FakeImageDetection/train/"
dirs = os.listdir( path )

#count number of sub-folders
def fcount(path):
    count1 = 0
    for root, dirs, files in os.walk(path):
            count1 += len(dirs)
    return count1

#resize the larger images
def resize():
    for item in dirs:
        for filename in os.listdir(path+item):
            if os.path.isfile(path+item+'/'+filename):
                for i in range(0,2):
                    img_org = cv2.imread(path+item+'/'+filename)
                    h , w, c = img_org.shape
                    if w>1920 and h>1080:
                        scale = 0.25
                    elif w>1280 and h>720:
                        scale = 0.75
                    else:
                        scale = 1
                    width  = int(img_org.shape[1]*scale)
                    height  = int(img_org.shape[0]*scale)
                    dimension  = (width,height)
                    im = Image.open(path+item+'/'+filename)
                    file, ext = os.path.splitext(path+item+'/'+filename)
                    #print(f,e)
                    imResize = im.resize(dimension, Image.ANTIALIAS)
                    #imResize.save(f+'.jpg', 'JPEG', quality=95)
                    imResize.save(file + ext)
                    #rgb_im.save(file.replace("png", "jpg"), quality=95)

#print(fcount(path))
#print(path)
#print(dirs)
#resize()