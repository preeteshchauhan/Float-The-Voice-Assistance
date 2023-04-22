import requests
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


# OpenWeatherMap API key and base URL
api_key = "c273ebf4b4af8fa872174ea9e4104530"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

# ask user for the city name
print("Which city's weather do you want to know?")
speak("Which city's weather do you want to know?")
city = take_command().lower()

# complete URL with city name and API key
complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

# request the weather data from the OpenWeatherMap API
response = requests.get(complete_url)

# check if the response status code is OK (200)

if response.status_code == 200:
    data = response.json()
        # get the temperature, humidity and status of weather
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    status = data["weather"][0]["description"]
        # speak out the weather condition
    engine.say(f"The current weather condition in {city} is {status}. The temperature is {temp} degrees Celsius and humidity is {humidity}%.")
    engine.runAndWait()
else:
    print("Could not retrieve weather data from OpenWeatherMap API.")
    engine.say("Sorry, I could not retrieve weather data for the specified city.")
    engine.runAndWait()
        
