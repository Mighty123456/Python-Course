import cv2

img = cv2.imread("image.jpg")

gaussian = cv2.GaussianBlur(img, (7, 7), 0)
median = cv2.medianBlur(img, 7)

cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)
cv2.destroyAllWindows()
