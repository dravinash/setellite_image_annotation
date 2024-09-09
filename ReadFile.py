import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = str(pow(2,40))
import cv2 as cv

PATH = 'Sample_Village/581304/581304_PANASPETA_GTIFF.tif'
img = cv.imread(PATH, cv.IMREAD_LOAD_GDAL)

cv.imshow('NYC', img)

cv.waitKey(0)
cv.destroyAllWindows()