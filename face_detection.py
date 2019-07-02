import cv2

camera = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier("cascades/haarcascade_frontalface_alt.xml")

if camera.isOpened():
    while True:
        ret, frame = camera.read()
        faces = face_classifier.detectMultiScale(frame, 1.3, 5, cv2.CASCADE_SCALE_IMAGE)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imshow('Detector', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
else:
    print("Camera is not opening, try again.")

camera.release()  # don't forget to do this.
cv2.destroyAllWindows()