import smtplib
import pyttsx3
from float import take_command
from email.message import EmailMessage

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
dict = {"float":"321preetesh0048@dbit.in"}
dict = {"flute":"321preetesh0048@dbit.in"}

def send_mail(receiver,subject,body):
    server = smtplib.SMTP("smtp.gmail.com",578)
    server.starttls()
    server.login("preeteshchauhan28@gmail.com","fgguseqwuojgkusy")
    email = EmailMessage()
    email["From"] = "preeteshchauhan28@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(body)
    server.send_message(email)
    
def main_poc():
    speak("To whom do you want to send your email?")
    name = take_command()
    receiver = dict[name]
    speak("Speak the subject of the email")
    subject= take_command()
    speak("Speak the body of the email")
    body = take_command()
    send_mail(receiver,subject,body)
    print("Your email has been send")
    
main_poc()
     
    
