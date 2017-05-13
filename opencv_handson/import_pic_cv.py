# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np

def readImg( fname ):
    img = cv2.imread( fname )
    cv2.imshow(fname, img)
    cv2.waitKey(0)

if __name__ == '__main__':

    finfo = sys.argv[1]
    print finfo
    readImg( finfo )
