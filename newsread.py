import requests
import json
import pyttsx3
import speech_recognition as sr
from float import take_command

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=093d6c17a5ef4ace899a09a3ebe7109f",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=093d6c17a5ef4ace899a09a3ebe7109f",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=#here paste your api keyhttps://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=093d6c17a5ef4ace899a09a3ebe7109f",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=093d6c17a5ef4ace899a09a3ebe7109f",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=093d6c17a5ef4ace899a09a3ebe7109f",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=093d6c17a5ef4ace899a09a3ebe7109f"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    r = sr.Recognizer()
    field = take_command()                    #input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 0 to stop]: ")
        if str(a) == "1":
            pass
        elif str(a) == "0":
            break
        
    speak("thats all")