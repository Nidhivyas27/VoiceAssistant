from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import json

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = search_entry.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    lon = location.longitude
    lat = location.latitude
    result = obj.timezone_at(lng=lon, lat=lat)

    timezone = pytz.timezone(result)
    local_time = datetime.now(timezone)
    current_time = local_time.strftime("%I:%M %p")
    clock_label.config(text=current_time)
    time_label.config(text="CURRENT WEATHER")

    # weather
    api = f"http://api.weatherapi.com/v1/current.json?key=<YOURAPIKEY>={city}"

    json_data = requests.get(api).json()
    condition = json_data["current"]["condition"]["text"]
    temp = json_data["current"]["temp_c"]
    pressure = json_data["current"]["pressure_in"]
    humidity = json_data["current"]["humidity"]
    wind = json_data["current"]["wind_kph"]

    Temperature.config(text=(temp, "°"))
    Condition.config(text=(condition, "|", "Feels", "Like", temp, "°"))
    WL.config(text=wind)
    HL.config(text=humidity)
    PL.config(text=pressure)


# Search Box
search_image = PhotoImage(file='photos\\search_bar.png')
search_label = Label(root, image=search_image)
search_label.place(x=20, y=20)

search_entry = Entry(root, justify="center", width=17, font=("poppins", 18, "bold"), bg="#404040", border=0, fg="white")
search_entry.place(x=90, y=45)
search_entry.focus()

search_icon = PhotoImage(file='photos\\search.png')
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather, activebackground="#404040")
search_button.place(x=400, y=34)

# Weather Icon
logo_image = PhotoImage(file='photos\\weather.png')
logo_label = Label(image=logo_image)
logo_label.place(x=220, y=90)

# Bottom box
bottom_image = PhotoImage(file='photos\\box.png')
bottom_label = Label(image=bottom_image)
bottom_label.pack(padx=5, pady=5, side=BOTTOM)

# Time
time_label = Label(root, font=("Arial", 15, "bold"))
time_label.place(x=30, y=100)

clock_label = Label(root, font=("Arial", 15, "bold"))
clock_label.place(x=30, y=130)

# Label
wind_label = Label(root, text="WIND", font=("poppins", 15, "bold"), fg="white", bg="#1ab5ef")
wind_label.place(x=120, y=400)

humidity_labe = Label(root, text="HUMIDITY", font=("poppins", 15, "bold"), fg="white", bg="#1ab5ef")
humidity_labe.place(x=390, y=400)

pressure_labe = Label(root, text="PRESSURE", font=("poppins", 15, "bold"), fg="white", bg="#1ab5ef")
pressure_labe.place(x=650, y=400)

Temperature = Label(font=("Arial", 70, "bold"), fg="#ee666d")
Temperature.place(x=450, y=150)

Condition = Label(font=("Arial", 15, "bold"))
Condition.place(x=450, y=250)

WL = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
WL.place(x=120, y=430)

HL = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
HL.place(x=400, y=430)

PL = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
PL.place(x=670, y=430)

root.mainloop()
