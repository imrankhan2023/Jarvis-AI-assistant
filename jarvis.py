import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning Imran khan sir! have a nice day!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon Imran sir! have a nice day!")
    else:
        speak("Good Evening Imran khan sir! have a nice day!")

    speak(" I Am Jarvis ...! your AI assistant , How can i help you sir")

def takeCommand():

    #it takes microphone inputs from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recogniging...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Could you please repeat it again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('imrankhan65462@gmail.com', '*********')
    server.sendmail('imrankhan65462@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # takeCommand()
   # speak("Hello Imran khan")
    # while True:
    while True:
      query = takeCommand().lower() #converting user query into lower case

      #   Logic for executing tasks bsed on query

      if 'wikipedia' in query: #if wikipedia is found in the query this block will be excecuted
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)


      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
    
      elif 'open google' in query:
          webbrowser.open("google.com")
    
      elif 'open facebook' in query:
          webbrowser.open("facebook.com")

      elif 'play music' in query:
          music_dir = 'C:\\Users\IMRAN KHAN\\Music\\Songs'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))

      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Hello Sir, now the time is {strTime}")

      elif 'open code' in query:
          codePath = "C:\\Users\\IMRAN KHAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

      elif 'email to imran khan' in query:
          try:
              speak("What should i say ?")
              content = takeCommand()
              to = "inandasimrankhan01@gmail.com"
              sendEmail(to, content)
              speak("Email has been sent succesfully! to imran khan sir!")

          except Exception as e:
              print(e)
              speak("I am extremly Sorry sir, There was an error in sending email")

           
  




     

        
