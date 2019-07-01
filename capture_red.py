import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
	status,frame=cap.read()
	cv2.inRange(frame,(0,0,0),(40,40,255))
	# cv2.inrange(frame,(0,0,0),(15,15,255))-----vary this and check
	cv2.imshow('liveredcolor', frame)
	if cv2.waitKey(10) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
