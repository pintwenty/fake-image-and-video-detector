from PIL import Image
import os, sys
import cv2
from glob import glob


def resize(path):


            if os.path.isfile(path):
                for i in range(0,2):
                    img_org = cv2.imread(path)
                    h , w, c = img_org.shape
                    if w>1920 and h>1080:
                        scale = 0.25
                    elif w>=1280 and h>=720:
                        scale = 0.75
                    else:
                        scale = 1
                    width  = int(img_org.shape[1]*scale)
                    height  = int(img_org.shape[0]*scale)
                    dimension  = (width,height)
                    im = Image.open(path)
                    f, e = os.path.splitext(path)
                    imResize = im.resize(dimension, Image.ANTIALIAS)
                    imResize.save(f+e)
