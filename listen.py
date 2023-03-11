import speech_recognition as sr  
from googletrans import Translator 

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #8 sec ke liye voice input lega woh
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")  #english me input ke liye en-US use hoga

    except:
        return ""    #kuch input nhi mila toh returns null
    
    query = str(query).lower()
    return query

Listen()

print(Listen())

def TraslationHintoEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(F"You: {data}.")
    return data

def MicExecution():
    query = Listen()
    data = TraslationHintoEng(query)
    return data

MicExecution()
