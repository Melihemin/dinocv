import cv2
import glob

path_1 = "data/1/"
path_0 = "data/0/"

files_1 = glob.glob(path_1 + "*.png")
files_0 = glob.glob(path_0 + "*.png")

image = cv2.imread(files_0[0])

imghold = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imghold, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('Screen', thresh)
# cv2.imshow('Old', image)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()