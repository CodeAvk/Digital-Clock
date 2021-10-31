
from tkinter import *
import time
app_window = Tk()
app_window.title("@Avk Digital Clock")
app_window.geometry("420x350")
app_window.resizable(1,1)
app_window.minsize(560,70)

background = "black"
foreground= "cyan"
border_width = 25

label = Label(app_window, font="DS-Digital  80 ", bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%I:%M:%S %p")
   label.config(text=time_live)
   label.after(1000, digital_clock)

digital_clock()
app_window.mainloop()