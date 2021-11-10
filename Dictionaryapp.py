#import all modules
#use pip install PyDictionary to install 
from tkinter import *
from PyDictionary import PyDictionary

#make objects
dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")

#function to show meaning,synonym,antonym
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][10])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

Label(root,text="Dictionary", font="lucida 20 bold", fg="green").pack(pady=10)

#frame 1
frame = Frame(root)
Label(frame, text="Type your word", font="lucida 20 bold", fg="skyblue4").pack(side=LEFT)

word = Entry(frame,font="lucida 15 bold")
word.pack()

frame.pack(pady=10)

#frame 2
frame1 = Frame(root)
Label(frame1,text="Meaning : ",font="lucida 10 bold").pack(side=LEFT)

meaning = Entry(frame1,font="lucida 15 bold",text="")
meaning.pack()

frame1.pack(pady=10)

#frame3
frame2 = Frame(root)
Label(frame2,text="Synonym : ",font="lucida 10 bold").pack(side=LEFT)

synonym = Entry(frame2,font="lucida 15 bold",text="")
synonym.pack()

frame2.pack(pady=10)

#frame 4
frame3 = Frame(root)
Label(frame3,text="Antonym : ",font="lucida 10 bold").pack(side=LEFT)

antonym = Entry(frame3,font="lucida 15 bold",text="")
antonym.pack(side=LEFT)

frame3.pack(pady=10)

Button(root,text="Submit",font="lucida 15 bold",command=dict).pack()

root.mainloop()
