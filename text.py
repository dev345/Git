import tkinter as tk
from gtts import gTTS
from playsound import playsound

q=tk.Tk()
q.title("Text To Speech")
q.geometry("200x70")
def text():
    text=entry.get()
    speech=gTTS(text=text,lang="en")
    speech.save(r'C:\Users\91889\Desktop\speech.mp3')
    playsound(r'C:\Users\91889\Desktop\speech.mp3')
label=tk.Label(q,text="Enter Here :")
label.grid(row=0,column=0)
entry=tk.Entry(q)
entry.grid(row=1,column=1)
button=tk.Button(q,text="Go",command=text)
button.grid(row=2,column=1)
q.mainloop()
