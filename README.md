# :musical_note: EMOSIC

This project under 'Face Recognition' category, enables the user to get song recommendations based on their emotion/mood. It detects the users emotion/mood and gives him a list of songs that can be directly played on platforms like Youtube, Spotify and Gaana.



# :hammer: Built With

Streamlit-This application uses Streamlit succeeded by a locally hosted html and css file.



# :pushpin: Getting Started

Instructions to set up local host

 ### Prerequisites
 ```bash
      pip install -r requirements.txt
 ```
The requirements.txt file in the repo gives the list of libraries to be installed inorder to run the files

### Installation
To clone the repo
```bash
git clone https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system.git
```
To run the main.py file on a web browser enter the following command in console
```bash
streamlit run filepath [ARGUMENTS]
```


# :file_folder: Screenshots

### This is a screenshot of the index.html file(here opened using Firefox) this file has animated background

![](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/Screenshots/preview%20ss/index.JPG)

### This is the next page which takes inputs

![](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/Screenshots/preview%20ss/main.JPG)



# :clipboard: About files

####    :paperclip:    The [datacollection.py](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/datacollection.py) file

Used to collect data and save in a .npy file.It requires access to your webcam. The [Collected data](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/tree/main/Collected%20data) folder gives the data collected on my device.

####    :paperclip:    The [data_training.py](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/data_training.py) file

Used to train the model and find its accuracy and loss, saves the model in a .h5 file and labels in a .npy file. The output files are [model.h5](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/model.h5) and [labels.npy](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/labels.npy)

####    :paperclip:    The [data_inference.py](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/data_inference.py) file

Used to infer the data and working of the model and prints the emotion in the terminal

####    :paperclip:   The [index.html](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/index.html) file

The first page of the website

####    :paperclip:   The [main.py](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/main.py) file

Built using stream lit gives recommendations to user and stores the array in [emotion.npy](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/emotion.npy) file.

####    :paperclip:   The [Output.md](https://github.com/ChiduruppalaPooja/EMOSIC-Emotion-based-music-recommendation-system/blob/main/Outputs.md) file
This gives the screenshots of all the .py files and the preview of the application

