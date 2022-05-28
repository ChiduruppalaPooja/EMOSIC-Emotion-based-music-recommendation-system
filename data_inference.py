#import necessary libraries
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model 

#load models
model  = load_model("model.h5")
label = np.load("labels.npy")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

#open camera 
cap = cv2.VideoCapture(0)


while True:
	list = []

	_, frm = cap.read() #reading one image

	frm = cv2.flip(frm, 1)

	result = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))   #processing the collected frame


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

		list = np.array(list).reshape(1,-1)     #convert list to a 2D array

		predictions = label[np.argmax(model.predict(list))]			#max prediction is collected 

		print(predictions)
		cv2.putText(frm, predictions, (50,50),cv2.FONT_ITALIC, 1, (255,255,0),2)		#print prediction on frameq

		
	drawing.draw_landmarks(frm, result.face_landmarks, holistic.FACEMESH_CONTOURS)
	drawing.draw_landmarks(frm, result.left_hand_landmarks, hands.HAND_CONNECTIONS)
	drawing.draw_landmarks(frm, result.right_hand_landmarks, hands.HAND_CONNECTIONS)

	cv2.imshow("window", frm)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		cap.release()
		break