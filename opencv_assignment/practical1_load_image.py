import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found. Check file name and path.")
    exit()

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
