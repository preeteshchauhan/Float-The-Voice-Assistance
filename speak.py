import pyttsx3

"""def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',200)  #SPEED OF THE ASSISTANCE
    print("")
    print(f"You: {Text}.")
    print("")
    engine.say(Text)
    #engine.save_to_file('')
    engine.runAndWait()"""

#Speak("Hello sir ")

from selenium import webdriver 
from selenium.webdriver.support.ui import Select        #yaha chrome ke funcitons karre hai- 
from selenium.webdriver.chrome.options import Options   #-hum import
from selenium.webdriver.common.by import By
from time import sleep

chrome_options= Options()
chrome_options.add_argument('--log-level=3')  #overprinting nhi hoga selenium ki taraf se
chrome_options.headless = True                #chrome open hoga but dikhega nhi
Path = "Databases\chromedriver.exe"
driver = webdriver.Chrome(Path,options= chrome_options)
driver.maximize_window()

website =r"https://ttsmp3.com/text-to-speech/British%20English/"  
driver.get(website)                 #chrome ko command diya hai ye website pe janne ke liye
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')   #brain sound hai woh change kar sakte hai



def Speak(Text):
    lengthoftext = len(str(Text))

    if lengthoftext==0:                  #Agar kuch nhi input mila toh just pass
        pass

    else:
        print("")
        print (f"Float: {Text}.")           # yaha text print hoga
        print("")
        Data = str(Text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'    
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)  #data woh website wale box me jayega
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click() #onclick read wala button hoga press
        driver.find_element(By. XPATH, value="/html/body/div[4]/div[2]/form/textarea").clear() #yaha box hoga clear
        
        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55: 
            sleep(8)
        elif lengthoftext>=70:
            sleep(10)
        elif lengthoftext>=100: 
            sleep(13)
        elif lengthoftext>=120: 
            sleep(14)
        else:
            sleep(2)
            
#Speak("Hello everyone")