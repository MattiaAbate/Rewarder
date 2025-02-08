# Rewarder

import tkinter as tk
from time import sleep
import pyperclip
import keyboard
from research import *

root = tk.Tk()
root.title("Rewarder")

root.geometry("400x300")

title = tk.Label(root, text="Rewarder", font=("Helvetica", 16))
title.pack(pady=20)

label = tk.Label(root, text="After closing this window\npress Enter to copy the research", font=("Helvetica", 12))
label.pack(pady=20)

def update_research():
    research = create_research()[0]
    research_label.config(text=f"Research: {research}")
    pyperclip.copy(research)

button = tk.Button(root, text="Example!", command=update_research)
button.pack(pady=20)

research_label = tk.Label(root, font=("Helvetica", 12))
research_label.pack(pady=20)

time = 0

root.mainloop()

print("Press Enter to start copying researches!\n")

while True:
    try:
        if keyboard.is_pressed('enter'):
            research = create_research()[0]
            url = create_research()[1]

            pyperclip.copy(research)
            time += 1

            print(f" - ({time}) Research: {research}\n\tURL: {url}")
            sleep(0.25)
    except:
        break