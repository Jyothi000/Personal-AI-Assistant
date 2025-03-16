import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()

root.title("AI Assistant")
root.geometry("500x600")
root.resizable(False, False)
root.config(bg="#6f8faf")
    
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_value = action.Action(user_val)
    text.insert(END, 'Me---->'+user_val+"\n")
    if bot_value != None:
        text.insert(END,"BOT<---"+str(bot_value)+"\n")
    if bot_value =="ok man":
        root.destroy()
    
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'Me---->'+send+"\n")
    if bot != None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot =="ok man":
        root.destroy()

def del_text():
    text.delete('1.0', "end")
    
frame = LabelFrame(root, padx=100 , pady=7 ,borderwidth=3 ,relief="raised")
frame.config(bg="#6f8faf")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label=Label(frame, text="AI Assistant", font=("Arial", 14, "bold"))
text_label.grid(row=0, column=0, padx=20, pady=10)

image = ImageTk.PhotoImage(Image.open("ai.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=10)

text = Text(root, font= ('courier 10 bold') , bg ="#356696")
text.grid(row= 2 , column= 0)
text.place(x= 100, y=320 , width=300 ,height = 100)

entry = Entry(root, justify=CENTER)
entry.place(x=100 , y=450 ,width=300, height=30)



button1 =  Button(root,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command= ask)
button1.place(x= 70, y= 510)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command= send)
button2.place(x= 320, y= 510)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID, command=del_text)
button3.place(x= 188.5, y= 510)

root.mainloop()



