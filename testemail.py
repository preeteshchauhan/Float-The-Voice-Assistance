import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listenser = sr.Recognizer()
tts = pyttsx3.Engine()


def talk(text):
    tts.say(text)
    tts.runAndWait()
    
def mic():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listenser.listen(source)
        data = listenser.recognize_google(voice)
        print(data)
        return data.lower()
    
    
email_dict = {"float": "321preetesh0048@dbit.in", "henry": "hendrychettier0005@gmail.com"}


def send_mail(receiver,subject,body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("preeteshchauhan28@gmail.com","fgguseqwuojgkusy")
    email = EmailMessage()
    email["From"] = "preeteshchauhan28@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)
    
def main_poc():
    talk("To whom do you want to send your email?")
    name = mic()
    receiver = email_dict[name]
    talk("Speak the subject of the email")
    subject= mic()
    talk("Speak the body of the email")
    body = mic()
    send_mail(receiver,subject,body)
    print("Your email has been send")
    
main_poc()