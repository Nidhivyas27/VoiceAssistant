# Importing necessary modules
from tkinter import *
from PIL import Image, ImageTk
import calendar


def year_GUI():
    def year_calendar():
        # Get the year entered in the entry widget
        year = int(year_entry.get())

        # Generate the calendar for the year and insert it into the text area
        data = calendar.calendar(year)
        text_Area.delete(0.0, END)
        text_Area.insert(INSERT, data)

    # Create the main window
    root = Tk()
    root.title("YEAR CALENDAR")
    root.geometry("755x650+200+30")
    root.config(bg="#F8F6F0")

     # Adding logo image to GUI
    logoImage = Image.open("photos\\cal.png")
    logoImage = logoImage.resize((45, 45), resample=Image.LANCZOS)
    logoImage = ImageTk.PhotoImage(logoImage)

    # Create the Calendar label
    text_label = Label(root, text="CALENDAR", font=("Arial", 14, "bold"), bg="#F8F6F0", image=logoImage)
    text_label.place(x=10, y=15)

    # Create the Year label
    year_Label = Label(root, text="Year", font=("Arial", 14, "bold"), bg="#F8F6F0")
    year_Label.place(x=70, y=25)

    # Create the Year entry widget
    year_entry = Entry(root, width=10, font=("Arial", 14, "bold"))
    year_entry.place(x=70, y=55)

    # Create the Show button
    show_Button = Button(root, text="Show", font=("Arial", 14, "bold"), command=year_calendar)
    show_Button.place(x=220, y=45)

    # Create the frame to hold the text area and scrollbar
    frame = Frame(root, bg="#F8F6F0")
    frame.place(x=10, y=100)

    # Create the scrollbar
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)

    # Create the text area to display the calendar
    text_Area = Text(frame, width=80, height=30, fg="black", yscrollcommand=scroll.set, bg="#F8F0E3")
    text_Area.pack(side=LEFT, expand=1)

    # Configure the scrollbar to work with the text area
    scroll.config(command=text_Area.yview)

    # Start the main event loop
    root.mainloop()

year_GUI()