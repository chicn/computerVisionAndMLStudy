import cv2
import sys
import numpy as np

def readImg( fname, flag = 0):
    img = cv2.imread( fname )
    if flag == 0:
        cv2.imshow(fname, img)
        cv2.waitKey(0)

    return img

if __name__ == '__main__':
    img = readImg( sys.argv[1], 1 )
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

    gray = np.float32(gray)
    dst = cv2.cornerHarris( gray, 2, 3, 0.04 )

    dst = cv2.dilate( dst, None )

    img[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    print "log"