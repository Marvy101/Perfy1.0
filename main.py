import sys
import threading
from datetime import *
import time
#import pyttsx3
from os_ops import *
from online_ops import *
import speech_recognition as sr
import random
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
"""Play from YouTube
   GUI
   Time wasting check
   """


USERNAME = "Marvy"
BOTNAME = "Perfy1.0"
'''
SPEAK_RATE = 164
engine = pyttsx3.init('sapi5')


# Set Rate
engine.setProperty('rate', 164)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice(Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech conversion


def say(text):

    engine.say(text)
    engine.runAndWait()
'''

def greet_user():
    hour = datetime.now().hour

    if (hour >= 1) and (hour < 12):
        say("Good Morning " + USERNAME)
    elif (hour >= 12) and (hour < 16):
        say("Good Afternoon " + USERNAME)
    elif (hour >= 16) and (hour <= 23):
        say("Good Evening " + USERNAME)
    else:
        say("It is Midnight, I do not know which one to say. Anyways,")



def take_userinput():
    times = 0
    while True:


        try:
            opening_text = ["Cool, I'm on it", "Okay, working on it",
                            "Please give me a minute, but you know I don't need a minute",
                            "Searching, Interpreting, Compiling, Bring results to the table ",
                            "Cooking the Results in a second",
                            "Do you know I can never get tired?",
                            "Over the past century, Michael has been the most popular male baby name 44 times",
                            "Just so you don't forget, I am the best assistant you will ever get",
                            "Just saying, my name is Perfy1.0",
                            "Do you know how high mount everest is? check it while I bring your answers."]

            """Takes User input as speech and converts to text, using the speech recognition module"""
            
            r = sr.Recognizer()
            with sr.Microphone() as source:
                tik1 = time.time()
                update_label("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            update_label("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            tok1 =  time.time()
            if (tik1-tok1)>1:
                say(random.choice(opening_text))
            update_label(query)
            if 'exit' in query or 'stop' in query:
                hour = datetime.now().hour
                if hour >= 20:
                    say("If you are going to bed now, Goodnight!, if not, Enjoy the rest of your night")
                else:
                    say("Bye!! .Enjoy the rest of your day!!")
                    exit()
            if query != '':
                #speak(choice(opening_text))
                if 'open Word' in query:
                    open_word()
                elif 'Wikipedia' in query:
                    w = sr.Recognizer()
                    say("Opening Wikipedia. Wikipedia accepts only one word")
                    with sr.Microphone() as source:
                        update_label("Listening...")
                        w.pause_threshold = 1
                        audio = w.listen(source)
                    update_label("Searching...")
                    tok2 = time.time()
                    if (tik1 - tok2) > 50:
                        say(random.choice(opening_text))
                    wiki_query = w.recognize_google(audio, language='en-in')
                    update_label(long_search_on_wikipedia(wiki_query))
                    say(search_on_wikipedia(wiki_query))
                elif 'open Chrome' in query:
                    open_chrome()
                elif 'open calculator' in query:
                    open_calc()
                elif 'open command prompt' in query:
                    open_cmd()
                elif 'Google' in query:
                    g = sr.Recognizer()
                    say("Speak, your servant is listening")
                    with sr.Microphone() as source:
                        update_label("Listening...")
                        g.pause_threshold = 1
                        audio = g.listen(source)
                    update_label("Searching...")
                    g_query = g.recognize_google(audio, language='en-in')
                    tok3 = time.time()
                    if (tik1 - tok3) > 50:
                        say(random.choice(opening_text))
                    (search_on_google(g_query))
                elif 'weather' in query:
                    say(get_weather_reports())
                elif 'temperature' in query:
                    say(get_temperature())
                elif 'news' in query:
                    say(get_latest_news())
                elif 'your name' in query:
                    say("My name is Perfy 1.0")
                    update_label("My name is Perfy 1.0")
                elif 'open clock' in query:
                    open_clock()
                elif 'tic tac toe' in query:
                    open_XO()
                elif 'your name' in query:
                    say("My name is Perfy 1.0")
                    update_label("My name is Perfy 1.0")
                elif 'bye' or 'good-bye' :
                    say("Bye, have a great day")

                    return 0
                elif  'end' or 'break':
                    say("Bye, have a great day")
                    update_label("Off, Press On to wake me.")
                    return 0



                time.sleep(3)
                times = times + 1


            if times > 2:
                say("Do you want to continue?")
                d = sr.Recognizer()
                with sr.Microphone() as source:
                    update_label("Listening...")
                    d.pause_threshold = 1
                    audio = d.listen(source)
                update_label("Searching...")
                d_query = d.recognize_google(audio, language='en-in')

                if 'yes' in d_query:
                    continue
                else:
                    update_label("Off, Press On to wake me.")
                    break


        except Exception:
            say("Couldn't recognise, please try again or Check your connection")
            time.sleep(5)


def onn():
    take_userinput()

def off():
    sys.exit()

window = Tk()
window.geometry("375x612")
window.title("Perfy 1.0")
window.configure(bg = "#EC0808")
canvas = Canvas(
    window,
    bg = "#EC0808",
    height = 812,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1452.0,
    1037.0,
    fill="#E0E2E3",
    outline="")
image_image_1 = PhotoImage(
    file=("image_1.gif"))
image_1 = canvas.create_image(
    187.0,
    220.0,
    image=image_image_1
)
canvas.create_text(
    70.0,
    0.0,
    anchor="nw",
    text=" PERFY 1.0",
    fill="#1A56EE",
    font=("RobotoSlab Bold", 36 * -1))
# On Button
button_image_1 = PhotoImage(
    file=("button_1.gif"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command = onn,
    relief="flat",
    text="On/Off"
)
button_label = Label(window, text="ON",fg="white" )
button_label.config(bg="#3c51f0")
button_label.pack()
button_label.place(
    x=40.0,
    y=565.0,
    width=75.0,
    height=24.0)
button_1.place(
    x=13.0,
    y=555.0,
    width=135.0,
    height=42.0
)
def update_label(texte):
    labelacious = Label(window, text=texte)
    labelacious.pack()
    labelacious.place(
        x=40.0,
        y=310,
        width=300.0,
        height=230.0
    )
    labelacious.update()


window.update()
window.resizable(False, False)
window.attributes('-alpha',0.93)
window.mainloop()
update_label("")