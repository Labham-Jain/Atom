# Importing Speech Recognition Library as 'sr' Keyword
import speech_recognition as sr
# Importing pyttsx3 To Speak Text
import pyttsx3

# Initalising pyttsx3 as engine

engine = pyttsx3.init()

# Creating Instance of Recognizer Class
recognizer = sr.Recognizer()

# Making 'Atom' class


class Atom:
    # Doing Some Documentation
    """
        This Package Provides Various Method To Use In Your Project Such As :

        1. Voice Recognition
        2. Speak Output

        Make Sure You Have The Following Modules Or Packages:

        1. SpeechReconition
        2. pyttsx3
    """
    # Making Constructor Or Init method

    def __init__(self):
        pass

    def Speak(self, Text):
        engine.say(Text)
        engine.runAndWait()

    def voiceRecognition(self, METHOD='Microphone'):

        # checking If METHOD Is 'Microphone'
        if METHOD == "Microphone":

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                # Printing "Starting Listening" To Terminal
                print("Starting Listening...")
                self.Speak("starting Listening...")
                listenedText = recognizer.listen(source)
                try:
                    print("Recognizing...")
                    self.Speak("Recognizing...")
                    voiceText = recognizer.recognize_google(
                        listenedText, language="en-US")
                    return voiceText
                except sr.UnknownValueError:
                    Atom().voiceRecognition()
        else:
            raise NotImplementedError
