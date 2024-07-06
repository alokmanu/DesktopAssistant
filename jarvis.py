import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import cv2
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)    
    if hour>= 0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")    
    else:
        speak("Good evening")  
    speak("I am Jarvis Sir. Please tell me how can I help you ")      
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_thresold =1
        audio=r.listen(source)
    try:
        print("Recognising...")    
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            print("Say that again please...")
            return "None"
    return query        

if __name__=="__main__":
    wishMe() 
    while True: 
        query=takeCommand().lower() 
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikikpedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')    
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com') 
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")               
            speak(f"sir, the time is {strTime}")
        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com') 
        elif 'open github' in query:
            webbrowser.open('github.com') 

        elif "open camer" in query:
            cam=cv2.VideoCapture(0)       
            while True:
                ret, frame = cam.read()
                cv2.imshow('mycam',frame)
                if cv2.waitKey(1)==ord('a'):
                    break
            reversed(frame)    


        
