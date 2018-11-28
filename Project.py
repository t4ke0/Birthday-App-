#Author = YASSINE MESSAOUDI ,  AKA : TAKEO
import os 
import sys
import tkinter as tk
from tkinter import * 
import datetime  
from datetime import date
from pygame import mixer 

window = tk.Tk()

window.title("Birthday")

window.geometry("600x500")

#---------------Function ---------------------------------
mixer.init()
mixer.music.load('C:/Users/yassine/Desktop/Birthday-App-/Music/50cent.mp3')#add path of this project were u clone it and Where the music file is . 
def Birth():
	now = datetime.datetime.now()
	if int(ent_2.get()) == int(now.day) and int(ent_3.get()) == int(now.month):
		mixer.music.play()
		return ("Happy Birthday " + str(ent_1.get()))	
	else :
		return ("Oops it's not currently your Birthday So make sure to come back later " + str(ent_1.get()))

def check_age():
	now = datetime.datetime.now()
	d0 = date(int(ent_4.get()),int(ent_3.get()),int(ent_2.get()))
	d1 = date(int(now.year),int(now.month),int(now.day))
	delta = d1 - d0
	Age = (float(delta.days)/365)
	output = round(Age, 1)
	return output

def celebrating_display():
	celeb = Birth()
	celebrating_display = tk.Text(master=window, heigh=5 , width= 50)
	celebrating_display.grid(column = 0 , row= 6)
	celebrating_display.insert(END,celeb)

def age_display():
	age = check_age()
	age_display = tk.Text(master=window,heigh=5,width=8)
	age_display.grid(column=0, row = 7)
	age_display.insert(END,age)

def reset():
	python = sys.executable 
	os.execl(python,python, * sys.argv)

#--------------LABEL--------------#------------------------------------
title = tk.Label(text="Birthday Application",font=("Serif",30))
title.grid()

inp_1 = tk.Label(text = "Please insert your Name: ")
inp_1.grid(column=0 , row =1 )

inp_2 = tk.Label(text = "Enter the day of your birth :")
inp_2.grid(column=0 , row=2)

inp_3 = tk.Label(text = 'Enter the month of your birth (2 digits): ')
inp_3.grid(column=0 , row=3)

inp_4 =tk.Label(text='Enter the Year were you born on it :')
inp_4.grid(column = 0 , row=4)

photo = PhotoImage(file="giphy.gif")
ph = Label(image=photo)
ph.grid(column=1 , row=0)
#------------ Entry ------#------------------------------------------
ent_1 = tk.Entry()
ent_1.grid(column = 1, row=1)

ent_2 = tk.Entry()
ent_2.grid(column = 1,row=2) 

ent_3 = tk.Entry()
ent_3.grid(column= 1 , row=3)

ent_4 = tk.Entry()
ent_4.grid(column= 1 , row=4)

#------------Check if is your Birthday Button--------#----------------------
b = tk.Button(text='Check your Birthday',bg="pink",command=celebrating_display)
b.grid(column = 1 , row= 5 )

b2 = tk.Button(text="Check your Age ! ", bg='green',command=age_display)
b2.grid(column=1 , row= 6)
#-------------------------------------------------------------------------
b3 = tk.Button(text='Reset',command=reset)
b3.grid (column=1, row=7)






window.mainloop()
