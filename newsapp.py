from tkinter import *
import requests
import webbrowser


# create function for the buttons
def read_news1(link1):
    webbrowser.open_new_tab(link1)

def read_news2(link2):
    webbrowser.open_new_tab(link2)

def read_news3(link3):
    webbrowser.open_new_tab(link3)

def read_news4(link4):
    webbrowser.open_new_tab(link4)

def read_news5(link5):
    webbrowser.open_new_tab(link5)

def read_news6(link6):
    webbrowser.open_new_tab(link6)

def read_news7(link7):
    webbrowser.open_new_tab(link7)
    
# make a list of the functions
news_list = [read_news1,read_news2,read_news3,read_news4,read_news5,read_news6,read_news7]

# url of the newsapi with your api key
url = 'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7858ec51ad7447219b1ee2bd7134d9ac&pagesize=7'


# get request of the newsapi
r = requests.get(url)
news = r.json()

# make an root object
root = Tk()
root.geometry('2000x2000')
root.config(background="skyblue")

# titel of the newsap
title = Label(root,text="Top News",font="lucida 30 bold")
title.pack()

# Make a loop to load your news
for newses,i in zip(news['articles'],news_list):
    Label(root,text=newses['title']).pack(anchor=NW,pady=5)
    Label(root,text=newses['description'],bg="orange",font="lucida 10 bold").pack(anchor=NW,pady=2,padx=2)
    new_button = Label(root,text="Read More",font="lucida 10 bold",bg='red')
    new_button.pack(anchor=NW)
    new_button.bind("<Button-1>",lambda e:i(newses['url']))
    root.update()

root.mainloop()