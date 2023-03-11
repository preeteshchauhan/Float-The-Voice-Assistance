from speak import Speak
from listen import Listen

def MainExe():
    
    while True:
        
        query = Listen()
        
        if "hello" in query:
            Speak("Hi! I am float how can i help you?")
            
        elif "bye" in query:
            Speak("Bye, have a nice day! ")