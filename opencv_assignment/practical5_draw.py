import cv2

img = cv2.imread("image.jpg")

cv2.line(img, (10, 10), (200, 10), (0, 255, 0), 3)
cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 3)
cv2.circle(img, (150, 150), 50, (0, 0, 255), 3)

cv2.imshow("Shapes on Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
