# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:19:25 2022

@author: 91870
"""

#VOICE ASSISTANT **J A R V I S**
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Speak Again")
            
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getPrperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
if __name__ == '__main__':
    
    if "hey jarvis" in sptext().lower():
        while True:
            data1 = sptext().lower()
            
            if "your name" in data1 :
                name = "my name is jarvis"
                speechtx(name)
                
            elif "old are you" in data1 : 
                age = "i am two years old"
                speechtx(age)
                
            elif 'time' in data1 :
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
                
            elif 'youtube' in data1 : 
                webbrowser.open("https://www.youtube.com/")
                
            elif 'web' in data1 : 
                webbrowser.open("https://www.google.com/")
                
            elif "joke" in data1 : 
                joke_1 = pyjokes.get_jokes(language = "en",catagory = "neutral")
                print(joke_1)
                
            elif 'play song' in data1 : 
                add = "E:\Songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[1]))
                
            elif "exit" in data1 : 
                speechtx("thank you")
                break
            
            time.sleep(10)
            
    else : 
        print("thanks")