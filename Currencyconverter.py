import requests
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

currency_list = ['INR','USD','AED','BHD','BRL','CAD','CNY','EUR','HKD','IDR','BGN','ILS','GBP','DKK','JPY','HUF','RON','MYR','SEK','SGD','CHF','KRW','TRY','HRK','NZD','THB','NOK','RUB','MXN','CZK','PLN','PHP','ZAR']

def CreateWidgets():
    inputAMT_Label = Label(root,text="AMOUNT : ",bg="peachpuff4")
    inputAMT_Label.grid(row=1,column=0,padx=5,pady=5)
    iAMT = Entry(root,width=14, textvariable=getAMT, bg="snow3",font=('',20), justify="center")
    iAMT.grid(row=1,column=2,padx=5,pady=5)

    fromLabel = Label(root,text="FROM : ", bg="peachpuff4")
    fromLabel.grid(row=2,column=0,padx=5,pady=5)
    root.fromList = Combobox(root, width=10, values = currency_list, state="readonly")
    root.fromList.set("INR")

    toLabel = Label(root,text="TO : ",bg="peachpuff4")
    toLabel.grid(row=2,column=2,padx=5,pady=5)
    root.toList = Combobox(root, width=10, values = currency_list, state="readonly")
    root.toList.grid(row=3,column=2,padx=5,pady=5)
    root.toList.set("INR")

    convertButton = Button(root,text="CONVERT",width=15, command=Convert)
    convertButton.grid(row=4,column=0, columnspan=3,pady=5,padx=5)

    extraLabel = Label(root,text="EXCHAGE RATE : ", bg="peachpuff4")
    extraLabel.grid(row=5,column=0,padx=5,pady=5,columnspan=2)
    root.exrate = Label(root,width=14,font=('',20),bg='snow3',justify="center")
    root.exrate.grid(row=5,column=2,padx=5,pady=5)

    outputLabel = Label(root,text="CONVERTED AMT : ",bg="peachpuff4")
    outputLabel.grid(row=6,column=0,pady=5,padx=5,columnspan=2)
    root.outputAMT = Label(root, width=14, font=('',20), bg="snow3",justify="center")
    root.outputAMT.grid(row=6,column=2, padx=5,columnspan=2)

def Convert():
    inputAmt = float(getAMT.get())
    from_Currency = root.fromList.get()
    to_Currency = root.toList.get()

    apiKey = "KYK8KQRZG4S984RO"
    baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    reqURL = baseURL+"&from_currency="+from_Currency+"&to_currency="+to_Currency+"&apikey="+apiKey

    response = requests.get(reqURL)
    result = response.json()
    exchangeRate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    root.exrate.config(text=str(round(exchangeRate, 2)))

    calculateAmt = round(inputAmt * exchangeRate, 2)
    root.outputAMT.config(text=str(calculateAmt))

root = tk.Tk()

root.geometry("350x250")
root.resizable(False,False)
root.title("Currency Converter")
root.config(bg="peachpuff4")

getAMT = StringVar()
fromCurrency = StringVar()
toCurrency = StringVar()

CreateWidgets()

root.mainloop()