import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

# create the main window
window = tk.Tk()
window.title('Digital Clock')
window.geometry("300x250")
window.config(bg="black")

# create the label for displaying the time
time_label = tk.Label(window, font=('calibri', 40, 'bold'), background='black', foreground='green')
time_label.pack(pady=20)

# call the update_time function to start updating the time
update_time()

# start the tkinter main loop
window.mainloop()
