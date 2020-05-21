import cv2
import os, sys
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip
def vid2jpg(img):
      path = img
      vidcap = cv2.VideoCapture(path)
      success,image = vidcap.read()
      count = 0
      #clip duration 
      clip = VideoFileClip(path)
      clip.close()
      duration = int(clip.duration)
      print("Seconds: {0}".format(duration))
      #clip fps
      fps = int(vidcap.get(cv2.CAP_PROP_FPS))
      print ("FPS:     {0}".format(fps))

      print("Estimated images : ",fps*duration)
      print("Analyzing Video. Please be patient!")
      while success:     
            cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG file
            success,image = vidcap.read()
            #print ('Read a new frame: ', success)
            count += 1
# copying frame10 from frames folder to test folder            
      src = "/Users/santh/PycharmProjects/FakeImage/venv/FakeImageDetection/frames/frame10.jpg"
      dst = "/Users/santh/PycharmProjects/FakeImage/venv/FakeImageDetection/test/"
      shutil.copy(src,dst)      
      
# deleting the images in frames folder
      folder = '/Users/santh/PycharmProjects/FakeImage/venv/FakeImageDetection/frames'
      for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                  if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                  elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
            except Exception as e:
                  print('Failed to delete %s. Reason: %s' % (file_path, e))

      print("Complete!")

#vid2jpg('/Users/santh/Desktop/vid2jpeg/1.mp4') 