
# coding: utf-8

# In[4]:


from Data_input_and_cleaning import *
from find_delay_flight import *
from Airline_info_avg import *


# In[24]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import ttk
import csv

#from pil import Image, ImageTk 

#extract host_id
with open('902101662_122017_63_airline_delay_causes.csv', 'r') as csvfile:
    content = csv.reader(csvfile.read().splitlines())
    airport = [row[5] for row in content]

with open('902101662_122017_63_airline_delay_causes.csv', 'r') as csvfile:
    content = csv.reader(csvfile.read().splitlines())
    aircode = [row[4] for row in content]
    
    print (airport)
csvfile.close()

#print (airport)

airport_dic= dict()
for x in range(1,len(airport)):
    if airport[x] in airport_dic:
        continue
    else:
        airport_dic[airport[x]] = aircode[x]
print (airport_dic) 


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

file_name = "902103314_112017_5253_airline_delay_causes.csv"
data = file_in(file_name)
dataClean = data_clean(data)

month_dict = {'Januray':1,'Feburary':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'Sepetember':9,'October':10,'November':11,'December':12}
    
global attackTime
attackTime=1

win = tk.Tk()
win.title("Airline Recommending System")    # title

ttk.Label(win, text="Choose a month").grid(column=1, row=0)    # Label
ttk.Label(win, text="Choose an airport").grid(column=0, row=0)      # Label location

# pull-down lists for Month
number1 = tk.StringVar()
numberChosen1 = ttk.Combobox(win, width=12, textvariable=number1)
numberChosen1['values'] = (" ","January", "Feburary", "March", "April", "May", "June", "July", "August","September", "October", "November", "December")     # 设置下拉列表的值
numberChosen1.grid(column=1, row=1)      
numberChosen1.current(0)  


# pull-down lists for Airports
number2 = tk.StringVar()
numberChosen2 = ttk.Combobox(win, width=50, textvariable=number2)
numberChosen2['values'] = tuple(airport_list)     
numberChosen2.grid(column=0, row=1)     
numberChosen2.current(0) 



# show when button is clicked 
def clickMe():  
    action.configure(text='Hello ' + numberChosen1.get())     # button content
    action.configure(state='disabled')      
    
def showMessage():
    top=tk.Toplevel()
    #top =tk.Tk()
    #function
    #input: month---numberChosen1.get()  airport---numberChosen2.get() airport code----- airport_dic[numberChosen2.get()]
   
    list_info=find_delay_flight(dataClean, month=month_dict[numberChosen1.get()],airport=airport_dic[numberChosen2.get()])
    rec_list = airline_info_avg(list_info)
    rec_sort = sorted(rec_list.items(),key=lambda item:item[1])
    
    
    
    #l=tk.Label(top,font=("黑体", 20, "bold"),text='Top 5 Recommending Airlines\n',width=40)
    #l=tk.Label(top,text = numberChosen2.get()+'\n'+numberChosen1.get(),width=40)
    tk.Label(top,fg = 'red',font = ("Arial", 20,"bold"), text = 'Top 5 Recommending Airlines',width=40).pack()
    for i in range(5):
        tk.Label(top,text = rec_sort[i][0]+'\n',width=40).pack()  
    top.mainloop()

# button
action = ttk.Button(win, text="Submit!", command=showMessage)    
action.grid(column=2, row=1)   


   

win.mainloop()     


