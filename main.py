from openai import OpenAI
import tkinter as tk
import os
from functools import partial
import base64

SS_PATH = "screenshot.png"  
openai = OpenAI()
PROMPT = "You are a multiple choice question answering bot. You will be given an image. With this image, parse the question, then return your answer. The answer should include an explanation, then finally at the end, return a single character that corresponds to the answer. This single character answer must be the absolute final character in the answer."

def takeScreenshot():
    os.system("screencapture -x -i screenshot.png")

def base64EncodeImage():
    with open(SS_PATH, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def getApiResponse():
    base64_image = base64EncodeImage()
    response = openai.chat.completions.create(
            model="gpt-4-turbo",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": PROMPT},
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )
    return response

def getAnswer():
    response_message = getApiResponse().choices[0].message.content
    answer = response_message[len(response_message) - 1]
    return answer

def resetAnswer(answer_label):
    answer_label.config(text="...")
    answer_label.update_idletasks()

def printAnswer(answer_label):
    resetAnswer(answer_label)
    answer = getAnswer()
    print(f"Answer: {answer}")
    answer_label.config(text=answer)
    
def createGuiWindow():
    window = tk.Tk()
    window.geometry('400x250')
    window.title("Snap Solve GPT4")

    answer_label = tk.Label(window, text="", font=('Helvetica', 80))
    answer_label.pack(side='bottom', pady=50)

    take_ss_btn = tk.Button(window,text="Take Screenshot",command=takeScreenshot)
    take_ss_btn.pack(side='top')

    get_answer_btn = tk.Button(window, text="Get Answer", command=partial(printAnswer,answer_label))
    get_answer_btn.pack(side='top')
    window.mainloop()

createGuiWindow()