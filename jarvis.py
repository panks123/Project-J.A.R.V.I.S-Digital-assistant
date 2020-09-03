import pyttsx3         #pyttsx3 is a text-to-speech conversion library in Python.
import speech_recognition as sr   #converts speech to text
import wikipedia
import webbrowser
import smtplib
import os
import subprocess
import pyautogui
import datetime
import calendar
from random import randint

engine=pyttsx3.init('sapi5')   #SAPI is an API developed by Microsoft to allow the use of speech recognition and speech
                              # synthesis within Windows applications.
voices=engine.getProperty('voices')
#print(voices)   ---two voices are available one of male and other of female
# print(voices[0].id)  ---DAVID's voice'
# print(voices[1].id)  ---ZIRA's voice
engine.setProperty('voice',voices[1].id)

def findDay(year,month,day):
    '''To get the week-day of a particular date'''

    #day, month, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])

def mailId(name):
    '''Returns the email id of the person'''
    dictMail={"pankaj":"pankajkumarhzb787@gmail.com",'aditya':'pankajadi'}
    if name in dictMail.keys():
        return dictMail[name]
    else:
        return  None

def sendEmail(to,content):
    '''to send an email to an email id'''

    server=smtplib.SMTP('smtp.gmail.com',587)  #587 is the port no.
    server.ehlo()
    server.starttls()
    server.login('pankajkumarhzb787@gmail.com','pankaj')
    server.sendmail('pankajkumarhzb787@gmail.com',to,content)
    server.close()

def speak(string):
    '''function which takes input as string and outputs the audio'''

    engine.say(string)
    engine.runAndWait()

def takeCommand():
    '''It takes microphone input returns string output'''

    r=sr.Recognizer() #Recognizer class helps in recognizing the command
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1   #Represents the minimum length of silence (in seconds) that will register
                              # as the end of a phrase.
        r.energy_threshold=305  #Represents the energy level threshold for sounds. Values below this threshold are
                                # considered silence, and values above this threshold are considered speech
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            print("Speak again...")
            return "None"

        return query

def wish():
    '''It will wish the user according to time'''

    hour=int(datetime.datetime.now().hour)  #value(0-24)
    if hour>=0 and hour<12:
        speak("Hello. Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("Hello. Good Afternoon!!!")
    else:
        speak("Hello. Good Evening!!!")
    speak("Could you please tell me your name")
    name=takeCommand().lower()
    if 'no' in name:
        speak("That's fine.")
        speak(f"I am Jarvis. How may I help you?")
    else:
        speak(f"I am Jarvis. How may I help you {name}?")

if __name__=='__main__':
    wish()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            print(query)
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia: ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query or 'open stack over flow' in query:
            webbrowser.open('https://stackoverflow.com')

        elif 'open gfg' in query or 'open geeks for geeks' in query or 'open geeksforgeeks' in query:
            webbrowser.open('https://www.geeksforgeeks.org/')

        elif 'play music' in query or 'play song' in query:
            music_dir="D:\\SOngs"
            songs=os.listdir(music_dir)
            random_song=randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[random_song]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {strTime}")

        elif 'open code' in query or 'open vs code' in query or 'open visual studio code' in query:
            code_path="C:\\Users\\Pankaj Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "send email" in query:
            speak("Whom to send?")
            try:
                name=takeCommand().lower()
                mailid=mailId(name)
                if mailid == None:
                    speak("Sorry! No such person exists.")
                else:
                    speak("What should I send?")
                    content=takeCommand()
                    sendEmail(mailid,content)
                    speak("Email sent.")
            except Exception as e:
                print("Sorry! The email could not be sent due to some problem.")
                speak("Sorry! The email could not be sent due to some problem.")
        elif 'today' in query or 'date' in query:
            dict_months={1:'January',2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",
                         9:"September",10:"Octobet",11:"November",12:"December"}
            current_time = datetime.datetime.now()
            year=current_time.year
            month=current_time.month
            tdate=current_time.day
            today=findDay(year,month,tdate)
            speak(f"Today is : {today}, {tdate} {dict_months[month]},{year}")

        elif 'who are you' in query:
            speak('I am JARVIS, I am a voice assistant.')

        elif 'open camera' in query:
            subprocess.run('start microsoft.windows.camera:', shell=True)

        elif 'open calculator'in query:
            subprocess.call(["calc.exe"])

        elif 'take screen shot' in query or 'take screenshot' in query :
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\Pankaj Kumar\Pictures\screenshot_fromPy\filename1.png')
            speak('screenshot captured')
        elif 'quit' in query or 'exit' in query:
            speak('Quitting! Happy to help!')
            exit()



