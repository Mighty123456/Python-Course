import cv2

img = cv2.imread("image.jpg")

cropped = img[50:200, 100:300]  # y1:y2, x1:x2

cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
