import os
import pyttsx3
import speech_recognition as sr

# create a text-to-speech engine object
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def open_file(file_path):
    try:
        os.startfile(file_path)
        speak("Opening the file")
    except Exception as e:
        print(e)
        speak("Sorry, I could not open the file")
        
# function to search a file in the computer system
def search_file():
    speak("What is the name of the file you are looking for?")
    file_name = take_command().lower()
    for root, dirs, files in os.walk('C:/'):  # change the directory path as per your system
        for name in files:
            if file_name in name.lower():
                file_path = os.path.join(root, name)
                speak(f"I found the file {name}.")
                open_file(file_path)
                return
    speak("Sorry, I couldn't find the file.")

# main function to control the voice assistant
if __name__ == "__main__":
    speak("Hi, I am your voice assistant. How can I help you?")
    while True:
        query = take_command().lower()
        if "search file" in query:
            search_file()
        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

    
        
        
        
        
