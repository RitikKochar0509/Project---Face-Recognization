import cv2

cap = cv2.VideoCapture(0)
face_Cascade = cv2.CascadeClassifier(r'C:\Users\ritik\Downloads\haarcascade_frontalface_alt.xml')


while True:
	ret,frame = cap.read()



	if ret==False:
		continue

	faces = face_Cascade.detectMultiScale(frame,1.3,5)

	for face in faces:
		x,y,w,h = face

		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0))
		cv2.imshow("Video Frame",frame)

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()