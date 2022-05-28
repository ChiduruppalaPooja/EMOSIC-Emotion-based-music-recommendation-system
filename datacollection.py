#import required libraries
import mediapipe as mp 
import numpy as np 
import cv2 
 
 #Accessing webcam to collect data
cap = cv2.VideoCapture(0)

name = input("Enter the name of the data : ")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

X = []
data_size = 0

while True:
	list = []

	_, frm = cap.read()				#read image from the camera

	frm = cv2.flip(frm, 1)

	result = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

	# face and hand landmarks

	if result.face_landmarks:
		for i in result.face_landmarks.landmark:
			list.append(i.x - result.face_landmarks.landmark[1].x)
			list.append(i.y - result.face_landmarks.landmark[1].y)

		if result.left_hand_landmarks:
			for i in result.left_hand_landmarks.landmark:
				list.append(i.x - result.left_hand_landmarks.landmark[8].x)
				list.append(i.y - result.left_hand_landmarks.landmark[8].y)
		else:
			for i in range(42):
				list.append(0.0)

		if result.right_hand_landmarks:
			for i in result.right_hand_landmarks.landmark:
				list.append(i.x - result.right_hand_landmarks.landmark[8].x)
				list.append(i.y - result.right_hand_landmarks.landmark[8].y)
		else:
			for i in range(42):
				list.append(0.0)


		X.append(list)
		data_size = data_size+1



	drawing.draw_landmarks(frm, result.face_landmarks, holistic.FACEMESH_CONTOURS)
	drawing.draw_landmarks(frm, result.left_hand_landmarks, hands.HAND_CONNECTIONS)
	drawing.draw_landmarks(frm, result.right_hand_landmarks, hands.HAND_CONNECTIONS)

	cv2.putText(frm, str(data_size), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2)
	 
	 #data being collected from webcam is shown

	cv2.imshow("window", frm) 

	if cv2.waitKey(1) == 27 or data_size>99:
		cv2.destroyAllWindows()
		cap.release()
		break

#Storing the data in a .npy file

np.save(f"{name}.npy", np.array(X))
print(np.array(X).shape)
        