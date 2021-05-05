import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randrange
import sys

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path),1) 


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # changes the voice





def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning Boss")
    elif hour>=12 and hour<=17:
        speak("Good After Noon Boss")
    else:
        speak("Good Evening Boss")
    speak("Jennifer at your service, how may i help you?")
    


def takeCommand():
    #take microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e) this will print the error

        ("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    
    wishMe()
    
    while True:
        query = takeCommand().lower()

    
    
        #logic for executing task based on query
        
        if "you there" in query or "are you listening" in query :
            speak("Yes sir, always")

        elif 'wikipedia' in query:
            speak("Searching wikipedia")
            query= query.replace('wikipedia'," ")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            
        elif "open youtube" in query:
            speak("opening youtube")
            url="https://www.youtube.com/"
            webbrowser.open(url)

        elif "open google" in query:
            speak("opening google")
            url='https://www.google.com'

            webbrowser.open(url)

        elif "open whatsapp" in query:
            url="https://web.whatsapp.com/"
            webbrowser.open(url)
            speak("opening whatsapp")
        
        elif "play music" in query or "play song" in query :
            speak("Do you want to play downloaded songs or online playlist?")
        elif "play downloaded"  in query or "downloaded songs" in query:
            music_dir= 'C:\\Users\\chait\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            n=len(songs)
            num=randrange(1,n)
            speak(f"playing {songs[num]}")
            os.startfile(os.path.join(music_dir, songs[num]))
        elif "play online" in query or "online songs" in query:
            speak("opening spotify")
            spotify="C:\\Users\\chait\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\spotify.exe"
            os.startfile(spotify)
        
        elif "play next" in query:
            if num==n-1:
                num=1
            else:
                num=num+1
            speak(f"playing {songs[num]}")
            os.startfile(os.path.join(music_dir, songs[num]))

                
        
        elif "time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "open teams" in query or "microsoft teams" in query:
            teams_path = "C:\\Users\\chait\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            os.startfile(teams_path)

        elif "where is" in query:
            query = query.split(" ")
            location = ""
            loc = query[2:len(query)]
            for i in loc:
                location = location +" " + i
                
            speak("showing you where " + location + " is.")
            url= "https://www.google.nl/maps/place/" + location
            webbrowser.open(url)

        elif "open chrome" in query:
            speak("opening chrome, sir")
            os.startfile(chrome_path)

        elif "land me to" in query or "take me to" in query:
            query = query.split(" ")
            location = ""
            loc = query[3:len(query)]
            for i in loc:
                location = location +" " + i
                
            speak("OK sir, let me take you to" + location)
            url= "https://earth.google.com/web/search/" + location
            webbrowser.open(url)


        elif "nothing" in query or "stop" in query  or "bye" in query:
            speak("okay")
            speak("Bye Sir, have a good day")
            sys.exit()
        
        
            


        
        


