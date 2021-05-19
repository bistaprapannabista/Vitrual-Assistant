import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
from datetime import date
import datetime
import wikipedia
import webbrowser
import random 
import subprocess

def speak(text):
    tts=gTTS(text,lang='en')
    filename="voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        print("Stop Listening")
        said=""
    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print("Exception: "+str(e))
    return said

speak("Hello")


text = get_audio()

if "bye" in text:
    speak("Bye sir, have a good day")

elif "hello" in text:
    speak("Welcome sir, it's Aagya here, How can I help you?")
    
    text2="start"
    while(text2!="stop"):
        text3=get_audio()
        if "date" in text3:
            today_int=date.today()
            today=str(today_int)
            speak(today)


        elif "time" in text3:
            now=datetime.datetime.now()
            now_int=now.strftime("%H:%M:%S")
            nowstr=str(now_int)
            speak(nowstr)
        
        elif "search" in text3:
            speak("What do you want to search in internet?")
            text5=get_audio()
            search=wikipedia.summary(text5, sentences=2)
            speak("According to wikipedia"+search)

        elif "website" in text3:
            speak("Which website you want to surf?")
            name=get_audio()
            webbrowser.open("https://"+name+".com")

        elif "dice" in text3:
            dice=str(random.randint(1,6))
            print(dice)
            speak("You got "+dice+"in dice")

        elif "toss" in text3:
            toss=random.randint(0,1)
            print(toss)
            if toss == 0:
                speak("You got Tail in toss")
            else:
                speak("You got Head in toss")

        elif "application" in text3:
            speak("Which application you want to launch?")
            app_name=get_audio()
            subprocess.Popen('C:\\Windows\\System32\\'+app_name+'.exe')

        elif "music" in text3:
            path='C:\\Users\\monst\\Music'
            music_list=os.listdir(path)
            os.startfile(os.path.join(path,music_list[1]))


        speak("Do you want to continue?")
        text4=get_audio()


        if "yes" in text4:
            text2="start"
        elif "no" in text4:
            text2="stop"
        else:
            speak("Sorry I can't get it, You must give commmand clearly otherwise I can't work")


speak("Thanks for using, see you again")


    



