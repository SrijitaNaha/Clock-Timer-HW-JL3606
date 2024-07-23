from tkinter import *
import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Countdown Timer App")

# Initialize timer variables
hours = 0
minutes = 0
seconds = 0
timer_running = False

# Create a function to update the timer
def update_timer():
    global hours, minutes, seconds, timer_running
    if timer_running:
        if seconds > 0:
            seconds -= 1
        elif minutes > 0:
            minutes -= 1
            seconds = 59
        elif hours > 0:
            hours -= 1
            minutes = 59
            seconds = 59
        else:
            timer_running = False
            timer_label.config(text="00:00:00")
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)

# Create a function to start the timer
def start_timer():
    global hours, minutes, seconds, timer_running
    get_hours = hour_entry.get()
    hours = int(get_hours)
    get_mins = minute_entry.get()
    minutes = int(get_mins)
    get_secs = second_entry.get()
    seconds = int(get_secs)
    timer_running = True
    start_button.config(state='disabled')
    hour_entry.config(state='disabled')
    minute_entry.config(state='disabled')
    second_entry.config(state='disabled')
    update_timer()

# Create a function to stop the timer
def stop_timer():
    global timer_running
    timer_running = False
    start_button.config(state='normal')
    hour_entry.config(state='normal')
    minute_entry.config(state='normal')
    second_entry.config(state='normal')

# Create entry boxes for hours, minutes, and seconds
hour_entry = tk.Entry(root, width=5)
minute_entry = tk.Entry(root, width=5)
second_entry = tk.Entry(root, width=5)
hour_entry.pack(side=tk.LEFT, padx=10)
minute_entry.pack(side=tk.LEFT, padx=10)
second_entry.pack(side=tk.LEFT, padx=10)

# Create a label to display the timer
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# Create Start and Stop buttons
start_button = tk.Button(root, text="Start", command=start_timer)
stop_button = tk.Button(root, text="Stop", command=stop_timer)
start_button.pack(side=tk.LEFT, padx=10)
stop_button.pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()