import requests
from bs4 import BeautifulSoup
import PIL.ImageTk,PIL.Image
import os
from tkinter import *

root = Tk()
url="https://www.worldometers.info/coronavirus/"
x = requests.get(url)
coronasoup = BeautifulSoup(x.text, 'html.parser')
coronadata = coronasoup.find_all("div", class_ = "maincounter-number") 
cases=coronadata[0].text.strip()
deaths=coronadata[1].text.strip()
rec=coronadata[2].text.strip()
    
def get_data():
    label1 = Label(root, text="Total Cases: "+cases+"\n Total Deaths: "+deaths+"\n Total Recovered: "+rec+".").pack(side="top")

def calc_death():
    strd=deaths.replace(',','')
    strc=cases.replace(',','')
    ndeath=float(strd)
    ncase=float(strc)
    rate=int((ndeath/ncase)*100)
    perc=str(rate)+" %"
    label2 = Label(root, text="Death Rate : "+perc+".").pack(side="bottom", padx=20)
    
img = PIL.ImageTk.PhotoImage(PIL.Image.open("download.jpg"))
panel = Label(root, image = img)
panel.pack(side = "left", fill = "both", expand = "yes")
   
show_button=Button(root, padx=20,pady=20, text="Display", command=get_data).pack(side = "left")
death_rate=Button(root, padx=20,pady=20, text="Death Rate", command=calc_death).pack(side = "left")
exit_button=Button(root, padx=30,pady=20, text="Exit", command=root.destroy).pack(side = "left")

root.mainloop()