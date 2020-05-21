import cv2

def CaptureImage():
    cam = cv2.VideoCapture(0)
    cam.set(1, 40)
    cam.set(1, 80)
    while True:
        ret, img = cam.read()
        cv2.imshow('Capture', img)
        cv2.imwrite(filename="../FakeImageDetection/test/cameraimg.jpg", img=img)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    print("\n close camera")
    cam.release()
    cv2.destroyAllWindows()

#CaptureImage()















