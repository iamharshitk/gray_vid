import cv2 as cv

vid=cv.VideoCapture("C:\\Users\\harsh\\Downloads\\123.mp4")

winname="Greyscale Video"

while True:
    ret, frame=vid.read()
    if not ret:
        break

    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.namedWindow(winname)

    cv.imshow(winname,cv.resize(gray_frame,(1080,720)))

    if cv.waitKey(1)==ord('q'):
        break

vid.release()
cv.destroyAllWindows()

