import cv2

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

_, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
