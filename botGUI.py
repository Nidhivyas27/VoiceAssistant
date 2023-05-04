from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr
import pyaudio
from VoiceAssistant import *
import subprocess
import threading
import keyboard
import spacy
import random
import json
import torch
from Brain import NeuralNetwork
from NeuralNET import Tokenized, Stems, bag_of_words
import pygame.mixer as mixer
import pygame

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("C:\\Users\\Admin\\OneDrive\\Desktop\\MyVoiceAssistant\\voiceenv\\intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "ChatbotData.pth" 
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

Name = "Emily"
reply = " "

askFild = ""
textArea = ""
message = " "
mic_Button = " "

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        textArea.insert(END, "Emily: Good Morning \n")
        # speak("Good Morning")
    
    elif 12 <= hour < 18:
        textArea.insert(END, "Emily: Good Afternon\n")
        # speak("Good Afternon")

    else:
        textArea.insert(END, "Emily: Good Evening\n")
        # speak("Good Evening")

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()

def IMG(tag, command):
    strng = message

    nlp = spacy.load("en_core_web_sm")

    doc = nlp(strng)
    for token in doc:
        if token.pos_ == "PROPN" or token.pos_ == "NOUN" or token.pos_ == "PRON" or token.ent_type_ == "PERSON" :
            if token.text.lower() not in ["image", "photo", "picture", "i", "me", "us", "them", "photos", "pic", "pics", "images", "pictures", "img", "imgs"]:
                entity = token.text
                webbrowser.open(f"https://www.google.com/search?q={entity}+image&rlz=1C1UEAD_enIN1012IN1012&sxsrf=APwXEde1_uqNy6216-ZfdL62u6-wIWNi0g:1682326462239&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi1_rW5ksL-AhUxTmwGHbizD-QQ_AUoAXoECAEQAw&biw=1366&bih=657&dpr=1")

def WIKI(tag, command):
    global textArea
    speak("Searching Wikipedia...")
    command = command.replace('wikipedia', " ").strip().lower()
    result = wikipedia.summary(command, sentences=3)
    speak("According to Wikipedia")
    msg = f"Emily: {result}\n"
    textArea.insert(END, msg)
    speak(result)

def Whatsapp(tag, command):
    global askFild, textArea, message
    # speak("What should I say")
    str_msg = "Hello this message is sent by Voice Assistant"
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1
    msg1 = f"Emily: wait for a minute\n"
    textArea.insert(END, msg1)
    kit.sendwhatmsg("WhatsApp_Number", str_msg, hour, minute)

def get_response(user_input):
    global reply, askFild
    result = str(user_input)
    if user_input == "bye":
        return "Goodbye!"

    sentence = Tokenized(user_input)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    probs = probs[0][predicted.item()]

    if probs.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    threading.Thread(target=subprocess.run, args=(['python', 'app\\TIME.py'],)).start()

                elif "date" in reply:
                    today = datetime.date.today()
                    reply = today.strftime("%B %d, %Y") # Format the date as a string

                elif "day" in reply:
                    reply = datetime.datetime.now().strftime("%A")

                elif "youtube" in reply:
                    webbrowser.open('https://www.youtube.com/')

                elif "google" in reply:
                    webbrowser.open('https://www.google.com/')

                elif "code" in reply:
                    os.startfile("C:\\Users\\Admin\\OneDrive\\Desktop\\VScode.exe")

                elif "pycharm" in reply:
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm.lnk")

                elif "music" in reply:
                    music_path = "songs"
                    songs = os.listdir(music_path)
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_path, song))

                elif "game" in reply:
                    reply = "Let's play"
                    time.sleep(0.5)
                    path1 = ['python', 'GAMES\\TicTacToe.py']
                    path2 = ['python', 'GAMES\\SnakeGame.py']
                    game_list = [path1, path2]
                    game = random.choice(game_list)
                    threading.Thread(target=subprocess.run, args=(game,)).start()

                elif "IP address" in reply:
                    reply = f"Your IP address is {requests.get('https://api.ipify.org/').text}"

                elif "joke" in reply:
                    reply = pyjokes.get_joke(language="en", category="all")

                elif "take photo" in reply or "take selfies" in reply:
                    reply = "Taking photo wait"
                    count = 0
                    stream = cv2.VideoCapture(0)
                    time.sleep(.5)
                    grabbed, frame = stream.read()
                    if grabbed:
                        cv2.imshow('pic', frame)
                        cv2.imwrite('pic' + f'{count+1}' + '.png', frame)
                    stream.release()
                    reply = "Photo is saved"

                elif f"image" in reply:
                    IMG(reply, result)

                elif "calendar" in reply:
                    threading.Thread(target=subprocess.run, args=(['python', 'app\\CalendaR.py'],)).start()

                elif "calculator" in reply:
                    threading.Thread(target=subprocess.run, args=(['python', 'app\\Calculator.py'],)).start()

                elif "search bar" in reply:
                    reply = "You can search here..."
                    threading.Thread(target=subprocess.run, args=(['python', 'app\\SearchBar.py'],)).start()

                elif "notepad" in reply:
                    threading.Thread(target=subprocess.run, args=(['python', 'app\\notepad.py'],)).start()

                elif "shutdown system" in reply:
                    reply = "Shutting down the system"
                    os.system('shutdown /r /t /s')

                elif "restart system" in reply:
                    reply = "restarting the system"
                    os.system("shutdown /r /t /s")

                elif "sleep system" in reply:
                    reply = "System going to sleep mode"
                    os.system("rundll32.exe powerproof.dll, SetSuspendState 0, 1, 0")

                elif "switch window" in reply:
                    reply = "switching the window"
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "play" in reply:
                    kit.playonyt(reply)

                elif "screenshot" in reply:
                    count = 0
                    file_name = count + 1
                    reply = "Hold on while I am taking screenshot"
                    time.sleep(1)
                    img = pyautogui.screenshot()
                    img.save(f"{file_name}.png")
                    reply = "Done, the screenshot is saved in our main folder."

                elif "wikipedia" in reply:
                    WIKI(reply, result)

                elif "volume up" in reply:
                    pyautogui.press("volumeup")
                
                elif "volume down" in reply:
                    pyautogui.press("volumedown")

                elif "volume mute" in reply:
                    pyautogui.press("volumemute")

                elif "whatsapp message" in reply:
                    Whatsapp(reply, result)

                elif "weather" in reply:
                    threading.Thread(target=subprocess.run, args=(['python', "app\\Weather.py"],)).start()

                else:
                  return reply

    return reply

def VOICE():
    global askFild, textArea, message

    pygame.mixer.init()
    mixer.music.load('notification.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=0.2)
            r.pause_threshold = 2.5
            r.energy_threshold = 100
            audio = r.listen(source, 0, 8)

            message = r.recognize_google(audio, language="en-in")

            askFild.delete(0, END)
            askFild.insert(END, message)
            msg1 = f"You: {message} \n"
            textArea.insert(END, msg1)

            askFild.delete(0, END)
            response = get_response(message)
            msg2 = f"Emily: {response}\n\n"
            textArea.insert(END, msg2)
            speak(response)

            mixer.music.load('notification2.mp3')
            mixer.music.play()
        
        except:
            textArea.insert(END, "Sorry, I didn't catch that \n Can you say that again... \n\n")
        # return message

def CLICk(*args):
    global askFild, textArea, message

    message = askFild.get()

    askFild.delete(0, END)
    askFild.insert(END, message)
    msg1 = f"You: {message} \n"
    textArea.insert(END, msg1)
    
    askFild.delete(0, END)
    response = get_response(message)
    msg2 = f"Emily: {response}\n\n"
    textArea.insert(END, msg2)

def COMMAND_LIST():
    os.startfile("command_list.txt")

def FEEDBACK():
    fb_root = Tk()
    fb_root.geometry("555x475")
    fb_root.title("Feedback")
    fb_root.config(bg="#82CAFF")

    Label(fb_root, text="Enter your feedback here:", font=("Times New Roman", 18, "bold"), bg="#82CAFF").pack(padx=5, pady=5)

    fb_name_label = Label(fb_root, bg="#82CAFF", fg="black", text="Name").pack(padx=2, pady=2)
    fb_add_name = Entry(fb_root, bg="white", fg="black", font=("Times New Roman", 18, "bold"), bd=8)
    fb_add_name.pack(padx=3, pady=3)

    fb_comment_label = Label(fb_root, bg="#82CAFF", fg="black", text="Add Feedback").pack(padx=2, pady=2)
    fb_add_comment = Text(fb_root, bg="white", fg="black", font=("Times New Roman", 18, "bold"), bd=8, width=30, height=10, wrap="word")
    fb_add_comment.pack(padx=3, pady=3)

    def SAVE_FB():
        name = fb_add_name.get()
        comment = fb_add_comment.get("1.0", "end-1c")
                
        with open("feedback.txt", "a") as f:
            f.write(f"Name: {name}\nFeedback: {comment}\n\n")

        fb_add_name.delete(0, END)
        fb_add_comment.delete("1.0", END)

        messagebox.showinfo("Thank You", "Thank you for your feedback!")

        fb_root.destroy()

    fb_submit_button = Button(fb_root, text="Submit", bg="white", fg="black", font=("Times New Roman", 18, "bold"), bd=8, command=SAVE_FB)
    fb_submit_button.pack(padx=5, pady=5)

    fb_root.mainloop()

def submit_feedback():
    feedback_thread = threading.Thread(target=FEEDBACK)
    feedback_thread.start()

def GUI():
    global askFild, mic_Button, textArea 

    root = Tk()

    root.geometry("855x625+100+100")
    root.title("Voice Assistant")
    root.config(bg="#FFA600")
    root.iconbitmap('photos\\EmilyAnimation.ico')

    main_menu = Menu(root)
    command_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Help", menu=command_menu)
    command_menu.add_command(label="Task", command=COMMAND_LIST)

    feedback_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Feedback", menu=feedback_menu)
    feedback_menu.add_command(label="Submit Feedback", command=submit_feedback)

    root.config(menu=main_menu)

    voice_logo = PhotoImage(file='photos\\Hotpot.png')
    logo_label = Label(root, image=voice_logo, bg="#FFA600", bd=8)
    logo_label.pack()

    text_Frame = Frame(root)
    text_Frame.pack()

    scroll = Scrollbar(text_Frame)
    scroll.pack(side=RIGHT, fill=Y)

    textArea = Text(text_Frame, font=("Times New Roman", 18, "bold"), height=9, yscrollcommand=scroll.set, bd=8, wrap="word")
    textArea.pack(side=LEFT, expand=1)
    scroll.config(command=textArea.yview)

    askFild = Entry(root, font=("Times New Roman", 18, "bold"), bd=8)
    askFild.pack(fill=X, pady=10)

    mic_logo = PhotoImage(file='photos\\icon.png')
    mic_Button = Button(root, image=mic_logo, bg="#FFA600", bd=0, command=VOICE)
    mic_Button.pack(pady=2)

    button = Button(root, text="Speak", font=("Times New Roman", 18, "bold"), fg="black", bd=0, bg="#FFA600", command=CLICk)
    button.pack()

    def Enter(event):
        button.invoke()

    root.bind('<Return>', Enter)

    WishMe()
    root.mainloop()

GUI()
