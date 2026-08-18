import cv2

cascade_path = r"E:\Python Programs\Python Course\opencv_assignment\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread("face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
