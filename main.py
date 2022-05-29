#import required libraries
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import webbrowser

st.set_page_config(page_title="EMOSIC", page_icon="🎶") #set page configuration

#load the label and model
model  = load_model("model.h5")
label = np.load("labels.npy")


holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

st.header("Emotion Based Music Recommender-EMOSIC")

if "run" not in st.session_state:
	st.session_state["run"] = "true"

try:
	emotion = np.load("emotion.npy")[0]
except:
	emotion=""

if not(emotion):
	st.session_state["run"] = "true"
else:
	st.session_state["run"] = "false"

#class called when webrtc_streamer is run

class EmotionProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")    #converting frames to array

		###############detect the landmarks and predict
		frm = cv2.flip(frm, 1)

		result = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

		lst = []

		if result.face_landmarks:
			for i in result.face_landmarks.landmark:
				lst.append(i.x - result.face_landmarks.landmark[1].x)
				lst.append(i.y - result.face_landmarks.landmark[1].y)

			if result.left_hand_landmarks:
				for i in result.left_hand_landmarks.landmark:
					lst.append(i.x - result.left_hand_landmarks.landmark[8].x)
					lst.append(i.y - result.left_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			if result.right_hand_landmarks:
				for i in result.right_hand_landmarks.landmark:
					lst.append(i.x - result.right_hand_landmarks.landmark[8].x)
					lst.append(i.y - result.right_hand_landmarks.landmark[8].y)
			else:
				for i in range(42):
					lst.append(0.0)

			lst = np.array(lst).reshape(1,-1)

			prediction = label[np.argmax(model.predict(lst))]

			print(prediction)
			cv2.putText(frm, prediction, (50,50),cv2.FONT_ITALIC, 1, (255,0,255),2)

			np.save("emotion.npy", np.array([prediction]))

			
		drawing.draw_landmarks(frm, result.face_landmarks, holistic.FACEMESH_TESSELATION,
								landmark_drawing_spec=drawing.DrawingSpec(color=(255,255,0), thickness=-1, circle_radius=1),
								connection_drawing_spec=drawing.DrawingSpec(thickness=1))
		drawing.draw_landmarks(frm, result.left_hand_landmarks, hands.HAND_CONNECTIONS)
		drawing.draw_landmarks(frm, result.right_hand_landmarks, hands.HAND_CONNECTIONS)


		##############################

		return av.VideoFrame.from_ndarray(frm, format="bgr24")


#to collect inputs from user

platform = st.selectbox("Select the app to listen",options=["Youtube" , "Spotify" , "Gaana"])
lang = st.text_input("Language")
singer = st.text_input("Singer/Artist")

st.write("Press enter to capture your emotion")

#opening the emotion detection widget

if platform and lang and singer and st.session_state["run"] != "false":
	webrtc_streamer(key="vpf", desired_playing_state=True,
				video_processor_factory=EmotionProcessor,media_stream_constraints={"video": True, "audio": False})

#adding button
btn2 = st.button("Recommend songs")


#recommendations
if btn2:
	if not(emotion):
		st.warning("Please let it capture your emotion first")
		st.session_state["run"] = "true"
	else:
		if platform == "Youtube":
			webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{emotion}+song+{singer}")
			
		elif platform == "Spotify":
			webbrowser.open(f"https://open.spotify.com/search/{lang}%20{singer}%20{emotion}%20songs")

		elif platform == "Gaana":
			webbrowser.open(f"https://gaana.com/search/{lang}%20{singer}%20{emotion}%20songs")

		np.save("emotion.npy", np.array([""]))
		st.session_state["run"] = "false"