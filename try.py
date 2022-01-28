import cv2

img = cv2.imread('data/data/Screenshot from 2022-01-25 22-26-01.png')

img = cv2.rectangle(img , (19,131), (56, 170), (0, 255, 0, 255), 1, cv2.LINE_AA)
img = cv2.rectangle(img , (417,141), (430, 169), (0, 255, 0, 255), 1, cv2.LINE_AA)

# [226, 139, 271, 171]
# 19	131	56	169	
cv2.imshow('asd',img)
cv2.waitKey(0)