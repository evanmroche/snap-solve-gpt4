from openai import OpenAI
import tkinter as tk
import os

SS_PATH = "screenshot.png"  

def takeScreenshot():
    os.system("screencapture -x -i screenshot.png")

def getAnswer():
    answer = "A"
    return answer 

def printAnswer():
    answer = getAnswer()
    print("Not functioning yet!")

def createGuiWindow():
    window = tk.Tk()
    window.geometry('400x250')
    window.title("Snap Solve GPT4")
    take_ss_btn = tk.Button(window,text="Take Screenshot",command=takeScreenshot)
    take_ss_btn.pack(side='top')

    get_answer_btn = tk.Button(window, text="Get Answer", command=printAnswer)
    get_answer_btn.pack(side='top')
    window.mainloop()


# DEf selectScreenshotArea():

createGuiWindow()