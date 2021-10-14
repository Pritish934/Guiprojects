from tkinter import *
#import calendar module
import calendar
#Make a root object
root = Tk()

#Function to show calendar
def showCal():
    y = int(year_var.get())
    cal = calendar.calendar(y)
    Label(root,text=cal,background="skyblue").pack()
    

root.geometry("600x700")
root.title("calender")

#Make a label to show calender to the top 
cal_label = Label(root,text="Calender", font="lucida 20 bold", background="grey",foreground="white")
cal_label.pack()

enter_label = Label(root,text="Enter year", font="lucida 12 bold", background="skyblue",foreground="red")
enter_label.pack()

#Create a yar variable to store the input of user
year_var = StringVar()
enter_entry = Entry(root,font="lucida 23 bold", foreground="black",background="skyblue4",textvariable=year_var)
enter_entry.pack()

#make a button
enter_button = Button(root,text="Enter",command=showCal,background="orange")
enter_button.pack()
#This is git change I made

root.mainloop()