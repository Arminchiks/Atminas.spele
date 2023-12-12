from email.mime import image
from tkinter import*#importē tkinter bibliotēku
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")
bgImg=ImageTk.PhotoImage(Image.open("7.png"))
#.resize((200.200),Image.ANTIALIAS)

#Izveido pogas - jābūt pāra skaitlim
btn0=Button(width=200,height=300,image=bgImg) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1=Button(width=200,height=300,image=bgImg)
btn2=Button(width=200,height=300,image=bgImg)
btn3=Button(width=200,height=300,image=bgImg)
btn4=Button(width=200,height=300,image=bgImg)
btn5=Button(width=200,height=300,image=bgImg)
btn6=Button(width=200,height=300,image=bgImg)
btn7=Button(width=200,height=300,image=bgImg)
btn8=Button(width=200,height=300,image=bgImg)
btn9=Button(width=200,height=300,image=bgImg)
btn10=Button(width=200,height=300,image=bgImg)
btn11=Button(width=200,height=300,image=bgImg)

#kopē pogas, maina skaitli

btn0.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=0,column=3)
btn4.grid(row=0,column=4)
btn5.grid(row=0,column=5)

btn6.grid(row=1,column=0)
btn7.grid(row=1,column=1)
btn8.grid(row=1,column=2)
btn9.grid(row=1,column=3)
btn10.grid(row=1,column=4)
btn11.grid(row=1,column=5)



myImg1=ImageTk.PhotoImage(Image.open("1.png"))
myImg2=ImageTk.PhotoImage(Image.open("2.png"))
myImg3=ImageTk.PhotoImage(Image.open("3.png"))
myImg4=ImageTk.PhotoImage(Image.open("4.png"))
myImg5=ImageTk.PhotoImage(Image.open("5.png"))
myImg5=ImageTk.PhotoImage(Image.open("6.png"))




gameWindow.mainloop()