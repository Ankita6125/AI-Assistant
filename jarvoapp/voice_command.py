import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"📥 You said: {query}")
    except:
        query = ""
    return query.lower()

def run_jarvo():
    command = take_command()
    if "youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {time}")
    else:
        talk("Sorry, I didn't understand.")
