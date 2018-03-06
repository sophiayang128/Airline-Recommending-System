
# coding: utf-8

# In[ ]:

#!/usr/bin/env python



import tkinter as tk
from tkinter import ttk
import csv

#from pil import Image, ImageTk 

#extract host_id
with open('902101662_122017_63_airline_delay_causes.csv', 'r') as csvfile:
    content = csv.reader(csvfile.read().splitlines())
    airport = [row[5] for row in content]
csvfile.close()

print (airport)

airport_set = set()
for x in range(1, len(airport)):
    if airport[x] in airport_set:
        continue
    else:
        airport_set.add(airport[x])

airport_list = list()
for x in airport_set:
    airport_list.append(x)
    
airport_list.sort()
airport_list.insert(0," ")
    
global attackTime
attackTime=1

win = tk.Tk()
win.title("Airline Recommending System")    # title

ttk.Label(win, text="Choose a month").grid(column=1, row=0)    # Label
ttk.Label(win, text="Choose an airport").grid(column=0, row=0)      # Label location

def show1():
    top1=tk.Toplevel()
    name = tk.StringVar()     
    nameEntered = ttk.Entry(win, width=12, textvariable=name)   
    #nameEntered.grid(column=0, row=1)      
    nameEntered.focus()    
    #image = Image.open('a.jpg') 
    #img = ImageTk.PhotoImage(image)
    #canvas1 = tk.Canvas(top1, width = image.width*2 ,height = image.height*2, bg = 'white')
    #canvas1.create_image(0,0,image = img,anchor="nw")
    #canvas1.create_image(image.width,0,image = img,anchor="nw")
    #canvas1.pack()   
    top1.mainloop()


# show when button is clicked 
def clickMe():  
    action.configure(text='Hello ' + name.get())     # button content
   #action.configure(state='disabled')      

# button
action = ttk.Button(win, text="Submit!", command=show1)    
action.grid(column=2, row=1)   


# pull-down lists
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (" ","January", "Feburary", "March", "April", "May", "June", "July", "August","September", "October", "November", "December")     # 设置下拉列表的值
numberChosen.grid(column=1, row=1)      
numberChosen.current(0)    

# pull-down lists
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=50, textvariable=number)
numberChosen['values'] = tuple(airport_list)     
numberChosen.grid(column=0, row=1)     
numberChosen.current(0)    

win.mainloop()

