import pyttsx3
import datetime
import time
import speech_recognition as sr
import win32api, sys, os
import wikipedia 
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
for i in voices:
    print(i)
engine.setProperty('voice' , voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def paswd():
    speak("Say Edith")
    query = take_commands().lower().strip()
    if(query == "edit" or query=="edith"):
        speak("Standby ..; Starting Biometric Scan; ")
        speak("Your Name")
        query = take_commands().lower().strip()
        speak("hello"+query)
        time.sleep(1)
        c=1   
    return c     
       

def wishme():
    t = int(datetime.datetime.now().hour)
    if(t>=0 and t<=12):
        speak("Good Morning.")
    elif(t>12 and t<=18):
        speak("Good Afternoon. ")
    else:
        speak("Good Evening .")
    speak("I am Edith. ")
    time.sleep(2)    

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)
        
    try :
        print("Recognizing......")
        query = r.recognize_google(audio , language = 'en-in')
        print("User Said:~  " + query)
    
    except Exception as e :
        print(e)
        speak("I am Not getting you , Say That Again")
        return "none"
    return query    

wishme()
speak("Fetching Files.... from Satellite 53;")
speak("Intializing Databases........;")
time.sleep(1)
speak(" Intializations SucessFull")
time.sleep(1)
c = paswd()


speak("Would u like to see what i can do; ")
while c :
    query = take_commands().lower()
    if 'yes' in query:
        speak("Than Say Open Youtube")
    elif (query == 'no'):
        speak("Ok! ; I am Quitiing")
        c=0
    elif 'wikipedia' in query:
        speak("Searching WEB.......")
        query = query.replace('wikipedia','')
        re = wikipedia.summary(query)
        print(re)
        speak(re)
    elif 'stop talking' in query:
        speak(" Quitting Sir...! Thanks for your time ")
        c=0    
    elif 'open youtube' in query:
        speak("here we go..")
        webbrowser.open("youtube.com")  
    elif 'about you' in query:
        speak("I am EDITH  and EDITH stands for Even Dead, I'm The Hero, I am developed By an Iron man Fan . U can Always Find My source code at github at abhi032 to make me smarter ")
    elif 'play music' in query:
        speak("Do u want to provide playlist path ?")
        query = take_commands().lower().strip()
        if "yes" in query:
            speak(" i am waiting for Path")
            x=input("Path")
            songs = os.listdir(x)
            print(songs)    
            os.startfile(os.path.join(x, songs[0]))
        else :
            speak("Sure...!! Playing......") 
            os.startfile("c:\\Users\\Abhishek\\Desktop\\Virtual_Assistant\\tmk.mp3") 

    elif 'google it' in query:
        speak("Sure!!!. opening web...")
        query = query.replace("google it","").strip()
        query = query.replace(" ","+")
        re = webbrowser.open("google.com/search?q="+query)
    else :
        speak("I am Not Allowed to do this ;")
        speak("Would You Like to Addd more features SO PLEASE ADD some commands")
        c=0    
