import speech_recognition as sr
import wikipedia
import datetime
import pyttsx3
import webbrowser
import os
import PyPDF2
import winshell
from tkinter import *
import smtplib
import pyjokes
import python_weather
import asyncio
from playsound import playsound
import requests
import wolframalpha

api_key= "87fd1cf253414f898c9c970ce7ec25f1 "


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    playsound(r"C:\Users\mayur\Downloads\futuresoundfx-13.mp3")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say again")
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('michelledesanta712@gmail.com', 'Qwertyuiop#123')
    server.sendmail('michelledesanta712@gmail.com', to, content)
    server.close()


async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.find("Washington DC")

    print(weather.current.temperature)
    speak(weather.current.temperature)

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    await client.close()


class widget:
    def __init__(self):
        root = Tk()
        root.title('Desktop Assistant')
        root.geometry('500x600')

        frameCnt = 50
        frames = [PhotoImage(file='lo.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label.configure(image=frame)
            root.after(100, update, ind)

        label = Label(root)
        label.pack()
        root.after(0, update, 0)

        userText = StringVar()
        userText.set('Desktop voice assistant')
        userFrame = LabelFrame(root, text='zeno', font=('cambria', 18, 'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='black', fg='purple')
        top.config(font=("cambria", 16))
        top.pack(side='top', fill='both', expand='yes')

        btn = Button(root, text='speak', font=('cambria', 14, 'bold'), bg='black', fg='red', command=self.clicked).pack(
            fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('cambria', 12, 'bold'), bg='red', fg='white',
                      command=root.destroy).pack(
            fill='x', expand='no')
        root.mainloop()

    def clicked(self):
        wishMe()
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open website' in query:
            speak("Which website to open")
            ws=takeCommand()
            webbrowser.open(f"{ws}.com")



        elif 'play music' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {strDate}")

        elif 'code' in query:
            codePath = "C:\\Users\\mayur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "calculate" in query:
            speak("what to you want to calculate")
            c = takeCommand()
            app_id = "T8WUEA-WT6K9YXKRK"
            client = wolframalpha.Client(app_id)

            res = client.query(c)
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "question" in query:
            speak("ask me")
            c = takeCommand()
            app_id = "T8WUEA-WT6K9YXKRK"
            client = wolframalpha.Client(app_id)

            res = client.query(c)
            answer = next(res.results).text
            speak(answer)

        elif 'email mayur' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mayureshngorantiwar@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ,I am unable able to send this email")


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")


        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('note.txt', 'w')
            file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'weather' in query:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(getweather())

        elif 'shutdown system' in query:
            speak("Just a sec!!system is shutting down")
            os.system("shutdown /s /t 1")

        elif 'read book' in query:
            book = open(r"C:\Users\mayur\Downloads\Call of Wild.pdf", 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages

            for num in range(1, pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                engine.say(text)
                engine.runAndWait()

        elif 'news' in query:
            main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
            news = requests.get(main_url).json()
            article = news["articles"]

            news_article = []
            for arti in article:
                news_article.append(arti['title'])

            for i in range(1):
                print(news_article)
                speak(news_article)

        else:
            speak("Sorry i did not understand")




if __name__ == '__main__':
    widget = widget()
