import cv2

img = cv2.imread("image.jpg")
resized = cv2.resize(img, (400, 400))

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
