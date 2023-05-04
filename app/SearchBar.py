# Importing necessary libraries
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import webbrowser
import speech_recognition as sr
import pyaudio
import pygame.mixer as mixer
import pygame


# Define a function to perform the search based on the selected search engine and the user's input
def SEARCH():
    if temp.get() != '':
        if temp.get() == 'google':
            webbrowser.open(f'https://www.google.com/search?q={search_area.get()}')

        elif temp.get() == "amazon":
            webbrowser.open(f'https://www.amazon.in/s?k={search_area.get()}&ref=nb_sb_noss')
    
        elif temp.get() == 'youtube':
            webbrowser.open(f"http://youtube.com/results?search_query={search_area.get()}")

    else:
        messagebox.showerror('Error', 'There is nothing to be searched')


# Define a function to perform voice recognition and fill the search area with the recognized speech
def Voice():
    # Load and play a notification sound before starting voice recognition
    pygame.mixer.init()
    mixer.music.load('notification.mp3')
    mixer.music.play()

    # Create a recognizer object and record audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            # Adjust for ambient noise before recording audio
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            
            # Use Google's speech recognition API to recognize the audio
            message = r.recognize_google(audio)

            # Clear the search area and insert the recognized speech
            search_area.delete(0, END)
            search_area.insert(END, message)

            # Perform the search using the recognized speech
            SEARCH()

            # Load and play a notification sound after the search is performed
            mixer.music.load('notification2.mp3')
            mixer.music.play()

        except:
            pass



# Create a new Tkinter window
root = Tk()

# Set the window properties
root.geometry("690x90+100+100")
root.title('Search Bar')
root.config(bg="black")
root.resizable(False, False)

# Create a StringVar object to store the selected search engine
temp = StringVar()

# Create a label for the search area
search_label = Label(root, text="Search", font=("Arial", 14, "bold"), bg="black", fg="white")
search_label.grid(row=0, column=0)

# Create an Entry widget for the user to input their search query
search_area = Entry(root, width=45, font=("Arial", 14, "bold"), bd=4, relief=SUNKEN, fg="black")
search_area.grid(row=0, column=1, sticky=W, padx=10)

# Load and resize an image for the microphone button
logoImage = Image.open("photos\\micro.png")
logoImage = logoImage.resize((32, 32), resample=Image.LANCZOS)
logoImage = ImageTk.PhotoImage(logoImage)

# Create a button for the user to activate voice recognition
micButton = Button(root, image=logoImage, bg="black", bd=0, cursor="hand2", command=Voice)
micButton.grid(row=0, column=2, sticky=W, padx=5)

# Load and resize an image for the search button
logoImage2 = Image.open("photos\\search.png")
logoImage2 = logoImage2.resize((32, 32), resample=Image.LANCZOS)
logoImage2 = ImageTk.PhotoImage(logoImage2)

# Create a button for the user to search 
searchButton = Button(root, image=logoImage2, bg="black", bd=0, cursor="hand2", command=SEARCH)
searchButton.grid(row=0, column=3, sticky=W, padx=5)

GoogleImage = Image.open("photos\\google.png")
GoogleImage = GoogleImage.resize((32, 32), resample=Image.LANCZOS)
GoogleImage = ImageTk.PhotoImage(GoogleImage)

# Set the style for the radio buttons
style = ttk.Style()
style.configure('TRadiobutton', background='black', foreground='white')

googleButton = ttk.Radiobutton(root, text="Google", value="google", variable=temp, image=GoogleImage, style='TRadiobutton')
googleButton.place(x=75, y=40)

AmazonImage = Image.open("photos\\amazon.png")
AmazonImage = AmazonImage.resize((32, 32), resample=Image.LANCZOS)
AmazonImage = ImageTk.PhotoImage(AmazonImage)

amazonButton = ttk.Radiobutton(root, text="Amazon", value="amazon", variable=temp, image=AmazonImage, style='TRadiobutton')
amazonButton.place(x=285, y=40)

YTImage = Image.open("photos\\youtube.png")
YTImage = YTImage.resize((32, 32), resample=Image.LANCZOS)
YTImage = ImageTk.PhotoImage(YTImage)

youtubeButton = ttk.Radiobutton(root, text="YouTube", value="youtube", variable=temp, image=YTImage, style='TRadiobutton')
youtubeButton.place(x=525, y=40)

# Setting up the default selected radio button value
temp.set('google')

# Binding the 'Return' key to the search button's functionality
def ENTER(event):
    searchButton.invoke()

root.bind('<Return>',ENTER)

# Starting the main event loop
root.mainloop()
