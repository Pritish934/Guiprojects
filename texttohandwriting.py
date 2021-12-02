import tkinter as tk
from tkinter import font
import pywhatkit as py
from PIL import Image as img
# Top level window
frame = tk.Tk()
frame.title("text to handwriting")
tk.Label(frame,text="Enter your sentence",font="lucida 20 bold").pack()
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget

def prinoutput():
    inp = inputtxt.get(1.0, "end-1c")
    py.text_to_handwriting(inp,save_to="sup.png", rgb=(0,0,138))
    im = img.open('sup.png')
    im.show()
    

	

# TextBox Creation
inputtxt = tk.Text(frame,
				width=100,
				)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Submit",
						command = prinoutput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
