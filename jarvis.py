import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')   #used for taking voices
voices = engine.getProperty('voices')
# print(voices[0].id)
# print("done")
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sameer")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sameer, at 1:45 you've to take your lunch")
    
    else:
        speak("Good Evening")
    
    speak("I am Jarvis. Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('sameerahmed3266@gmail.com', 'Dexter999@')
    server.sendmail("sameerahmed3266@gmail.com", to , content)
    server.close()



if __name__ == "__main__":
    # speak("Sameer is a good boy")
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in  query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "email to sameer" in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "sameerahmed3266@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry My Friend Sameer. I am not able to send this email")
