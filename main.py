import datetime
import os
import random
import subprocess
import time
import webbrowser
# name u void
import PyPDF2 as PyPDF2
import cv2
from gtts import gTTS
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from PyDictionary import PyDictionary
from playsound import playsound
from pytube import YouTube
from tkinter import *
from tkinter import messagebox, filedialog
from googletrans import Translator
from random import randint
import requests
from bs4 import BeautifulSoup
from requests import get
from pywikihow import search_wikihow

dictionary = PyDictionary()

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 180)
reply_to_thanks = ["You're welcome sir", "Always happy to Help!", "my pleasure sir"]
reply_to_hru = ["I am fine Sir!", "Top of the world sir", "As good as an AI assistant can be!",
                "sir you made me, you should know!", "I am doing great"]
reply_to_break_needed = ["Ok sir, you can call me anytime", "Bye Sir", "Yes Sir, I agree. Bye",
                         "taking break right now", "Your wish is my command sir! Bye"]
hour = datetime.datetime.now().hour
hour1 = int(datetime.datetime.now().hour)


def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"JARVIS: {audio}")
    print("  ")
    Assistant.runAndWait()


# noinspection PyBroadException
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"listening.....")
        command.pause_threshold = 2
        audio = command.listen(source)

        try:
            print(f"Recognising....")
            query = command.recognize_google(audio, language='en-in')
            print(f"SIDDHANT: {query}")

        except Exception as Error:
            #Speak("Say that again please")
            return "None"

        return query.lower()


def Wish_me():
    if hour1 >= 0 and hour1 <= 12:
        Speak("Good Morning")

    elif hour1 > 12 and hour1 < 6:
        Speak("Good afternoon")

    else:
        Speak("Good evening ")
    Speak("I am Jarvis")
    Speak("Your personal AI Assistant")
    Speak("How may I help you?")


if __name__ == "__main__":
    print("J.A.R.V.I.S Initiated")
    Speak("JARVIS Initiated")
    #Speak("")
    Wish_me()



def TaskExe():
    def Music():
        Speak("Sure! Tell me the song name")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)

    def RockPaperScissors():

        # create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        # assign a random play to the computer
        computer = t[randint(0, 2)]

        # set player to False
        player = False

        while player == False:
            # set player to True
            Speak("Choose rock, paper or scissors")
            playerChoice = takecommand()
            if 'rock' in playerChoice:
                player = "Rock"

            elif 'paper' in playerChoice:
                player = "Paper"

            elif 'scissors' in playerChoice:
                player = "Scissors"

            else:
                Speak("That's not a valid play. Check your spelling!")

            if player == computer:
                Speak("It's a tie, you chose" + player + "and Computer chose" + computer)

            elif player == "Rock":
                if computer == "Paper":
                    Speak("You lose!" + computer + "covers" + player)
                else:
                    Speak("You win!" + player + "smashes" + computer)
            elif player == "Paper":
                if computer == "Scissors":
                    Speak("You lose!" + computer + computer + "cut" + player)
                else:
                    Speak("You win!" + player + "covers" + computer)
            elif player == "Scissors":
                if computer == "Rock":
                    Speak("You lose..." + computer + "smashes" + player)
                else:
                    Speak("You win!" + player + "cut" + computer)

            # player was set to True, but we want it to be False so the loop continues
            Speak("Do you wanna play again")
            ChoicePlayAgain = takecommand()
            if 'yes' in ChoicePlayAgain or 'ya' in ChoicePlayAgain:
                ChoicePlayAgain = False

            else:
                ChoicePlayAgain = True
                Speak("Exited Rock Paper scissors")
            player = ChoicePlayAgain
            computer = t[randint(0, 2)]

    def Whatsapp():
        Speak("Tell me the name of the person to send the WhatsApp message to")
        name = takecommand()

        if 'dad' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg("+91 9619089263", msg, hour, mins, 8)
            Speak("OK Sir sending.......")

        elif 'mom' in name or 'mum' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg("+91 9619089262", msg, hour, mins, 8)
            Speak("OK Sir sending.......")

        elif 'jason' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg("+91 9082607664", msg, hour, mins, 8)
            Speak("OK Sir sending.......")

        elif 'tanishka' in name or 'germany' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg("+91 8369665548", msg, hour, mins, 8)
            Speak("OK Sir sending.......")

        elif 'sammriddhi' in name or 'sosa' in name or 'sam' in name or 'sammy' in name or 'sammwiddhi' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            # mins=mins.replace(" ", "")
            # mins=mins.replace("-", "")
            # mins=mins.replace("_", "")
            pywhatkit.sendwhatmsg("+91 9820719881", msg, hour, mins, 8)
            Speak("OK Sir sending.......")


        elif 'mama' in name:
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg("+1 (302) 559-1367", msg, hour, mins, 8)
            Speak("OK Sir sending.......")


        else:
            Speak("I don't know him/her tell Me The Phone number")
            PhoneNo = takecommand()
            ph = "+91" + PhoneNo
            Speak("Tell me what is the message?")
            msg = takecommand()
            Speak("Tell time in hour")
            hour = int(takecommand())
            Speak("Tell time in minutes now")
            mins = int(takecommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, mins, 8)
            Speak("OK Sir sending.......")

    def OpenApps():
        Speak("OK let me find it")
        if 'deliverables input' in query:
            webbrowser.open(
                "https://onedrive.live.com/edit.aspx?action=editnew&resid=471395B4839DF8BB!1767&ithint=file%2cxlsx&action=editnew&wdNewAndOpenCt=1615784389561&wdPreviousSession=0323529c-56ca-42c7-bb03-d2a21ad2963f&wdOrigin=OFFICECOM-WEB.START.NEW")
            Speak("Opening Deliverables")

        elif 'spotify' in query:
            os.startfile("C:\\Users\\user123\\AppData\\Roaming\\Spotify\\Spotify.exe")
            Speak("Opening Spotify")

        elif 'o b s' in query:
            os.startfile("C:\\Program Files\\obs-studio\\bin\64bit\\obs64.exe")
            Speak("Opening OBS studio")

        elif 'epic games' in query:
            os.startfile(
                "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
            Speak("Opening Epic Games for the epic gamer")

        elif 'unity' in query:
            os.startfile("C:\\Program Files\\Unity Hub\\Unity Hub.exe")
            Speak("Opening Unity Hub")
        else:
            Speak("App not found")

    def SpeedTest():
        import speedtest
        Speak("Checking Speed..........")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading / 800000)
        uploading = speed.upload()
        correctUploading = int(uploading / 800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUploading} mbps")

        elif 'downloading' in query:
            Speak(f"The downloading speed is {correctDown} mbps")

        else:
            Speak(f"The downloading speed is {correctDown} mbps and the uploading speed is {correctUploading} mbps")

    def Reader():

        Speak("Tell me the name of the book to read")

        name = takecommand()

        if 'geography' in name and 'notes' in name:

            os.startfile("C:\\Users\\user123\\Downloads\\STD X - GEOG - SAMPLE NOTES - SOIL.pdf")
            book = open("C:\\Users\\user123\\Downloads\\STD X - GEOG - SAMPLE NOTES - SOIL.pdf", 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in the book are {pages}")
            Speak("From which page do I have to start reading?")
            numPage = int(input("Enter No of pages here"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language do I have to read")
            lang = takecommand()

            if 'hindi' in lang:
                Speak("Ok reading in hind")
                transl = Translator()
                texthin = transl.translate(text, 'hi')
                textm = texthin.text
                speech = gTTS(text=textm)
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

    def Dict():
        Speak("Dictionary initiated")
        Speak("Tell me the problem")
        problem = takecommand()

        if 'meaning' in problem:
            problem = problem.replace("what is the", "")
            problem = problem.replace("jarvis", "")
            problem = problem.replace("of", "")
            problem = problem.replace("meaning", "")
            result = dictionary.meaning(problem)
            Speak(f"The meaning for {problem} is {result}")

        elif 'synonym' in problem or 'same word':
            problem = problem.replace("what is the", "")
            problem = problem.replace("jarvis", "")
            problem = problem.replace("of", "")
            problem = problem.replace("synonym", "")
            result = dictionary.synonym(problem)
            Speak(f"The synonym for {problem} is {result}")

        elif 'antonym,' in problem or 'opposite' in problem:
            problem = problem.replace("what is the", "")
            problem = problem.replace("jarvis", "")
            problem = problem.replace("of", "")
            problem = problem.replace("antonym", "")
            problem = problem.replace("opposite", "")
            result = dictionary.antonym(problem)
            Speak(f"The antonym for {problem} is {result}")

        Speak("Exited Dictionary")

    def CloseApps():
        Speak("OK, Sir, wait a second ")

        if 'youtube' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'stack overflow' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'github' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'white hat junior' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'deliverables' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'google translate' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'zoom' in query:
            os.system("TASKILL /F /im Zoom.exe")

        elif 'brave' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'browser' in query:
            os.system("TASKILL /F /im brave.exe")

        elif 'o b s' in query:
            os.system("TASKILL /F /im obs64.exe")

        elif 'spotify' in query:
            os.system("TASKILL /F /im Spotify.exe")

        elif 'unity' in query:
            os.system("TASKILL /F /im Unity Hub.exe")

        elif 'epic' in query:
            os.system("TASKILL /F /im EpicGamesLauncher.exe")

        elif 'blender' in query:
            os.system("TASKILL /F /im blender.exe")

        elif 'fortnite' in query:
            os.system("TASKILL /F /FortniteClient-Win64-Shipping.exe")

        elif 'whatsapp' in query:
            os.system("TASKILL /F /im WhatsApp.exe")

        Speak("Your command has been completed")

    def temp():
        search = "temperature in mumbai"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The temperature outside is {temperature}")

    def takeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"listening.....")
            command.pause_threshold = 2
            audio = command.listen(source)

            try:
                print(f"Recognising....")
                query = command.recognize_google(audio, language='hi')
                print(f"SIDDHANT: {query}")

            except Exception as Error:
                return "None"

            return query.lower()

    def trans():
        Speak("Tell me the line")
        line = takeHindi()
        ts = Translator()
        # result = ts.translate(line)
        if line:
            result = ts.translate(line)
            ResultText = result.text
            Speak("The translation for this text is: " + ResultText)

    def YoutubeAuto():
        Speak("What's your command")
        comm = takecommand()
        if 'pause' in comm:
            pyautogui.hotkey('k')

        elif 'restart' in comm:
            pyautogui.hotkey('0')

        elif 'mute' in comm:
            pyautogui.hotkey('m')

        elif 'forward' in comm:
            pyautogui.hotkey('l')

        elif 'back' in comm:
            pyautogui.hotkey('j')

        elif 'full screen' in comm:
            pyautogui.hotkey('f')

        elif 'theatre mode' in comm:
            pyautogui.hotkey('t')

        elif 'skip' in comm:
            pyautogui.hotkey('shift', 'n')

        Speak("Done Sir")

    def BraveAuto():
        Speak("Ok, what do you want me to do?")
        command = takecommand()

        if 'close this tab' in command or 'close tab' in command:
            pyautogui.hotkey('ctr;', 'w')

        if 'open a new tab' in command or 'new tab tab' in command:
            pyautogui.hotkey('ctr;', 't')

        if 'reload this tab' in command or 'reload tab' in command:
            pyautogui.hotkey('ctr;', 'r')

        if 'show my history' in command or 'show history' in command:
            pyautogui.hotkey('ctr;', 'h')

        if 'open a new window' in command or 'new window' in command:
            pyautogui.hotkey('ctr;', 'n')

        if 'open console' in command or 'console' in command:
            pyautogui.hotkey('ctr;', 'shift', 'i')

        if 'show downloads' in command or 'downloads' in command:
            pyautogui.hotkey('ctr;', 'j')

        if 'book mark this tab' in command or 'book mark' in command or 'bookmark' in command:
            pyautogui.hotkey('ctr;', 'd')

        if 'incognito' in command or 'go incognito' in command:
            pyautogui.hotkey('ctr;', 'shift', 'n')

        else:
            Speak("Error, command not found")

        Speak("Done Sir")

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir, I am Jarvis .")
            Speak("Your Personal AI Assistant! ")
            Speak("How may I help you?")

        elif 'how are you' in query:
            Speak(random.choice(reply_to_hru))
            Speak("What About You")

        elif 'you need a break' in query or 'bye' in query or 'take a break' in query:
            Speak(random.choice(reply_to_break_needed))
            break

        elif 'am' in query and "great" in query:
            Speak("That's nice sir")
            # just to close loop
            
            


        elif 'youtube search' in query:
            Speak("OK SIR Here is what I found!")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'greet' in query:
            query = query.replace("Jarvis", "")
            query = query.replace("greet", "")
            Speak("Hey," + query + ", How are you?")

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google", "")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("search", '')
            Speak("This is what I found on the web")
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query, 3)
                Speak(result)

            except:
                Speak("No speakable data found")

        elif 'launch website' in query:
            Speak("Ok Tell me name of website")
            Name = takecommand()
            Name.replace(" ", "")
            web = "https://www." + Name + ".com"
            webbrowser.open(web)
            Speak("Opened " + Name)

        elif 'thank you' in query or 'thanks' in query:
            Speak(random.choice(reply_to_thanks))
            # just to close loop

        elif 'open github' in query:
            Speak("Opening GitHub now!")
            webbrowser.open("https://github.com")

        elif 'open white hat junior' in query:
            Speak("Opening Whitehat Junior now!")
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")

        elif 'open youtube' in query:
            Speak("Opening YouTube now!")
            webbrowser.open("https://youtube.com")

        elif 'open google translate' in query:
            Speak("Opening Google Translate now!")
            webbrowser.open("https://translate.google.com/")

        elif 'open stack over flow' in query or 'open stack overflow' in query or 'open stackoverflow' in query:
            Speak("Opening StackOverflow now!")
            webbrowser.open("https://stackoverflow.com/")

        elif 'play a song' in query:
            Music()
            #

        elif "sign out" in query or 'logoff' in query or "log off" in query:
            Speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "shutdown" in query:
            Speak("Shutting down system")
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            Speak("Restarting system")
            os.system("shutdown /r /t 5")

        elif "sleep" in query:
            Speak("Going to sleep")
            os.system("rundll32.exe powrprof.dll , SetSuspendState 0,1,0")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia......")
            query = query.replace("Jarvis", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            ans = takecommand()
            Speak(f"According to Wikipedia : {wiki}")
            if "stop" in ans or "ok" in ans:
                break

        elif "mirror" in query or "show me" in query or 'show myself' in query:
            Speak("Opening image preview:)")
            Speak("Press Q To Quit")
            cam = cv2.VideoCapture(0)
            while (True):

                # Capture the video frame
                # by frame
                ret, frame = cam.read()

                # Display the resulting frame
                cv2.imshow('Image Preview', frame)

                # the 'q' button is set as the
                # quitting button you may use any
                # desired button of your choice
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # After the loop release the cap object
            cam.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

        elif 'whatsapp message' in query or 'send a whatsapp message' in query or 'WhatsApp message' in query:
            Whatsapp()
            #

        elif "capture" in query or "photo" in query or "pic" in query or 'picture' in query:
            Speak("Press 'P' to take a photo, esc to exit")
            cam = cv2.VideoCapture(0)
            while True:
                _, frame = cam.read()  # We don't want ret in this
                cv2.imshow("Image Preview", frame)  # Show the current frame
                key = cv2.waitKey(1)
                if key == 27:  # If you press Esc then the frame window will close (and the program also)
                    Speak("Exited Photo window")
                    break
                elif key == ord('p'):  # If you press p/P key on your keyboard
                    cv2.imwrite("C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\pic.png",
                                frame)  # Save current frame as picture with name pic.jpg
                    time.sleep(0.7)
                    Speak("Opening your picture now")
                    os.startfile("C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\pic.png")

            cam.release()
            cv2.destroyAllWindows()

        elif 'screenshot' in query or 'screen shot' in query:
            Speak("Screenshot taken and saved ,opening it now")
            pyautogui.screenshot('my_screenshot.png')
            time.sleep(0.3)
            os.startfile("C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\my_screenshot.png")


        elif 'open spotify' in query:
            OpenApps()

        elif 'open epic games' in query:
            OpenApps()

        elif 'open deliverables input' in query:
            OpenApps()

        elif 'open OBS studio' in query or 'OBS' in query:
            OpenApps()

        elif 'open Unity' in query or 'unity' in query:
            OpenApps()

        elif 'open Fortnite' in query or 'launch fortnite' in query:
            Speak("Launching Fortnite, this may take a while")
            pyautogui.click(x=602, y=1062)

        elif 'open Whatsapp' in query or 'open whatsapp' in query:
            os.startfile("C:\\Users\\user123\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            Speak("Opening WhatsApp")

        elif 'open Zoom' in query or 'open zoom' in query:
            os.startfile("C:\\Users\\user123\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            Speak("Opening Zoom")



        elif 'open blender' in query:
            os.startfile("C:\\Program Files\\Blender Foundation\\Blender 2.91\\blender.exe")
            Speak("Opening Blender")

        elif 'open vs code' in query or 'open vscode' in query:
            os.startfile("C:\\Users\\user123\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            Speak("Opening Visual Studio")

        elif 'open steam' in query:
            os.startfile("C:\\Program Files (x86)\\Steam\\Steam.exe")
            Speak("Opening Steam")

        elif 'open deliverables output' in query:
            webbrowser.open("https://technofrost27.github.io/spreadsheet/")
            Speak("Opening Deliverables Output Database")

        elif 'edit a photo' in query or 'open photoshop' in query:
            os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe")
            Speak("Starting Photoshop 2021")

        elif 'edit a video' in query or 'open premier pro' in query:
            os.startfile("C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe")
            Speak("Starting Premiere Pro 2020")

        elif 'full screen' in query and 'window' in query:
            Speak("Making this window fullscreen if supported ")
            pyautogui.hotkey('f11')

        elif 'max' in query and 'window' in query:
            Speak("Maximising current window")
            pyautogui.hotkey('alt', 'space')
            pyautogui.hotkey('x')

        elif 'restore' in query and 'window' in query:
            Speak("Restoring window to it's original size")
            pyautogui.hotkey('alt', 'space')
            pyautogui.hotkey('r')

        elif 'minimise' in query and 'window' in query:
            Speak("Minimising current window")
            pyautogui.hotkey('alt', 'space')
            pyautogui.hotkey('n')

        elif 'close' in query and 'window' in query:
            Speak("Closing current window")
            pyautogui.hotkey('alt', 'space')
            pyautogui.hotkey('c')

        elif 'switch windows' in query or 'switch window' in query or 'change windows' in query or 'alt tab' in query or 'all tab' in query:
            Speak("Switching Windows")
            pyautogui.hotkey('alt', 'tab')

        elif 'Show desktop' in query and 'windows d' in query:
            Speak("Here is the desktop")
            pyautogui.hotkey('win', 'd')

        elif 'task manager' in query:
            Speak("Opening task manager")
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif 'command prompt' in query:
            Speak("Opening command prompt as admin")
            pyautogui.hotkey('win', 'x')
            pyautogui.hotkey('a')
            time.sleep(0.6)

        elif 'close youtube' in query:
            CloseApps()

        elif 'close stack overflow' in query:
            CloseApps()

        elif 'close github' in query:
            CloseApps()

        elif 'close white hat junior' in query:
            CloseApps()

        elif 'close deliverables' in query:
            CloseApps()

        elif 'close google translate' in query:
            CloseApps()

        elif 'close brave' in query:
            CloseApps()

        elif 'close browser' in query:
            CloseApps()

        elif 'close o b s' in query:
            CloseApps()

        elif 'close spotify' in query:
            CloseApps()

        elif 'close zoom' in query:
            CloseApps()

        elif 'close unity' in query:
            CloseApps()

        elif 'close epic games' in query:
            CloseApps()

        elif 'close blender' in query:
            CloseApps()

        elif 'close fortnite' in query:
            CloseApps()

        elif 'close whatsapp' in query:
            CloseApps()

        elif 'youtube' in query and 'action' in query:
            YoutubeAuto()

        elif 'brave' in query and 'action' in query:
            BraveAuto()

        elif 'joke' in query or 'make me laugh' in query:
            getJoke = pyjokes.get_joke()
            Speak(getJoke)

        elif 'repeat this' in query or 'repeat after me' in query:
            Speak("Speak sir")
            repeatedCommand = takecommand()
            Speak(repeatedCommand)

        elif 'my location' in query:
            Speak("Ok, here is your location......")
            webbrowser.open(
                "https://www.google.co.in/maps/place/Megh+Tower,+Yashodham,+Goregaon,+Mumbai,+Maharashtra+400063/@19.1737215,72.8619565,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7b7a7c4a458d7:0xc036afcdd539602d!8m2!3d19.1737215!4d72.8641452!16s%2Fg%2F12hks6k21?hl=en")

        elif 'dictionary' in query:
            Dict()

        elif 'set an alarm' in query:
            Speak("Enter The Time")
            alarm_time = input("Enter the Time:")

            while True:
                Time_AC = datetime.datetime.now()
                now = Time_AC.strftime("%H:%M:%S")
                Speak("Alarm Set for " + alarm_time)
                if now == alarm_time:
                    Speak("Alarm Over")
                    playsound('alarm.mp3')

                elif now > alarm_time:
                    break

        elif 'video downloader' in query or 'download youtube video' in query:
            Speak("OK, Enter video URL and file location")

            def Widgets():
                link_label = Label(root,
                                   text="YouTube link  :",
                                   bg="#E8D579")
                link_label.grid(row=1,
                                column=0,
                                pady=5,
                                padx=5)

                root.linkText = Entry(root,
                                      width=55,
                                      textvariable=video_Link)
                root.linkText.grid(row=1,
                                   column=1,
                                   pady=5,
                                   padx=5,
                                   columnspan=2)

                destination_label = Label(root,
                                          text="Destination    :",
                                          bg="#E8D579")
                destination_label.grid(row=2,
                                       column=0,
                                       pady=5,
                                       padx=5)

                root.destinationText = Entry(root,
                                             width=40,
                                             textvariable=download_Path)
                root.destinationText.grid(row=2,
                                          column=1,
                                          pady=5,
                                          padx=5)

                browse_B = Button(root,
                                  text="Browse",
                                  command=Browse,
                                  width=10,
                                  bg="#05E8E0")
                browse_B.grid(row=2,
                              column=2,
                              pady=1,
                              padx=1)

                Download_B = Button(root,
                                    text="Download",
                                    command=Download,
                                    width=20,
                                    bg="#05E8E0")
                Download_B.grid(row=3,
                                column=1,
                                pady=3,
                                padx=3)

            def Browse():

                download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

                download_Path.set(download_Directory)

            def Download():

                Youtube_link = video_Link.get()

                download_Folder = download_Path.get()

                getVideo = YouTube(Youtube_link)

                videoStream = getVideo.streams.first()

                videoStream.download(download_Folder)

                messagebox.showinfo("SUCCESSFULLY",
                                    "DOWNLOADED AND SAVED IN\n"
                                    + download_Folder)
                Speak("Video Downloaded sir!")

            root = Tk()

            root.geometry("600x120")
            root.resizable(False, False)
            root.title("YouTube_Video_Downloader")
            root.config(background="#000000")

            video_Link = StringVar()
            download_Path = StringVar()

            Widgets()

            root.mainloop()

        elif 'what is the time' in query or "what's the time" in query or 'tell me the time' in query or 'what is the current time' in query:

            now = datetime.datetime.now()

            current_time = now.strftime("%H:%M:%S")

            if 0 <= hour < 12:
                Timed_Greeting = "morning!"

            elif 12 <= hour < 5:
                Timed_Greeting = "afternoon!"

            elif 5 <= hour < 9:
                Timed_Greeting = "evening!"

            else:
                Timed_Greeting = "night!"

            Speak(f"Current Time is {current_time}! Also have a great {Timed_Greeting}")

        elif 'copy text' in query or 'copy this' in query:
            pyautogui.hotkey('ctrl', 'c')
            Speak("Copied Text to clipboard! ")

        elif 'cut text' in query or 'cut this' in query:
            pyautogui.hotkey('ctrl', 'x')
            Speak("Cut text")

        elif 'paste text' in query or 'paste this' in query:
            pyautogui.hotkey('ctrl', 'v')
            Speak("Pasted text from clipboard!")

        elif 'mute' in query and 'teams' in query:
            pyautogui.hotkey('ctrl', 'shift', 'm')
            Speak("Ok, toggled mic")

        elif 'video' in query and 'teams' in query:
            pyautogui.hotkey('ctrl', 'shift', 'o')
            Speak("Ok, Toggled Video ")

        elif 'blur' in query and 'teams' in query:
            pyautogui.hotkey('ctrl', 'shift', 'p')
            Speak("Ok, blurred background")

        elif 'raise hand in teams' in query or 'raise my hand in teams' in query:
            pyautogui.hotkey('ctrl', 'shift', 'k')
            Speak("Ok sir, raised hand")

        elif 'leave meeting' in query or 'leave the meeting' in query:
            pyautogui.hotkey('ctrl', 'shift', 'b')
            Speak("Ok sir, left the meeting")

        elif 'translate' in query or 'translator' in query:
            trans()

        elif 'remember this' in query or 'remember that' in query:
            query = query.replace("remember this", "")
            query = query.replace("remember", "")
            query = query.replace("this", "")
            query = query.replace("that", "")
            query = query.replace("jarvis", "")
            remembermsg = query
            Speak("OK Sir, I will remember:" + remembermsg)
            remember = open('data.txt', 'w')
            remember.write(remembermsg)
            remember.close()

        elif 'what do you remember' in query or 'what did i tell you to remember' in query:
            remember = open('data.txt', 'r')
            Speak("I remember that: " + remembermsg)

        elif 'play' in query and ('rock' in query or 'paper' in query or 'scissors' in query):
            RockPaperScissors()

        elif 'Tell me the temperature' in query or 'what is the temperature' in query or 'temperature outside' in query:
            temp()

        elif 'read a book' in query or 'read me a book' in query or 'dictate a book' in query or 'read book' in query:
            Reader()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            Speak(f"Your IP Address is {ip}")

        elif 'speedtest' in query or 'speed test' in query or 'internet speed' in query:
            SpeedTest()

        elif 'download speed' in query or 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query or 'upload speed' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Getting data from the internet")
            query = query.replace("tell me", "")
            command = query.replace("Jarvis", "")
            max_reult = 1
            how_to_func = search_wikihow(command, max_reult)
            assert len(how_to_func) == 1
            # how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'volume up' in query or 'increase volume' in query:
            Speak("Increased volume by 2 points")
            pyautogui.press("volumeup")

        elif 'volume down' in query or 'decrease volume' in query:
            Speak("Decreased volume by 2 points")
            pyautogui.press("volumedown")

        elif 'mute' in query:
            Speak("Muted Volume")
            pyautogui.press("volumemute")

        elif 'mobile camera' in query:
            import urllib.request
            import numpy as np
            URL = "http://192.168.43.1:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWEBCAMERA', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;


            cv2.destroyAllWindows()


TaskExe()
