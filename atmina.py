from cgitb import enable
from email.mime import image
from tkinter import*#importē tkinter bibliotēku
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("Vienādie attēli")
bgImg=ImageTk.PhotoImage(Image.open("7.png"))
#.resize((200.200),Image.ANTIALIAS)
galvenaIzvelne=Menu(gameWindow)
gameWindow.config(menu=galvenaIzvelne)

def infoLogs():
    gameWindow=Toplevel()
    gameWindow.title("Par programmu")
    gameWindow.geometry('1055x200')
    desc=Label(gameWindow,text="Spēles mērķis ir iegūt vienādas bildes zem apslēptiem lodziņiem.",font='Helvita 26 bold')
    desc.grid(row=0,column=0)
    desc=Label(gameWindow,text="Uzspiežot uz jebkuru tu izvēlies bildi un tad tev ir jāuzspiež uz citu lodziņu,",font='Helvita 16')
    desc.grid(row=1,column=0)
    desc=Label(gameWindow,text="ja bildes nesakrīt, tad aizvērsies izvēlētās bildītes un būs viss jāizvēlas vēlreiz,",font='Helvita 16')
    desc.grid(row=2,column=0)
    desc=Label(gameWindow,text="ja bildes sakritīs, tad bildes paliks atvērtas un būs jāizvēlas jaunas, līdz attaisīsi visas bildītes",font='Helvita 16')
    desc.grid(row=3,column=0)
def reset():
    global count,correctAnswers,answers,answer_dict, answercount
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)

    btn0['image']='pyimage1'
    btn1['image']='pyimage1'
    btn2['image']='pyimage1'
    btn3['image']='pyimage1'
    btn4['image']='pyimage1'
    btn5['image']='pyimage1'
    btn6['image']='pyimage1'
    btn7['image']='pyimage1'
    btn8['image']='pyimage1'
    btn9['image']='pyimage1'
    btn10['image']='pyimage1'
    btn11['image']='pyimage1'
    random.shuffle(ImageList)
    answers=[]
    answer_dict={}
    count=0
    correctAnswers=0
    answercount=0
    return 0

opcijas=Menu(galvenaIzvelne,tearoff=False)
galvenaIzvelne.add_cascade(label='Opcijas',menu=opcijas)

opcijas.add_command(label='Jauna spēle',command=reset)
opcijas.add_command(label='Iziet',command=gameWindow.quit)


galvenaIzvelne.add_command(label='Par programmu',command=infoLogs)


#def



#Izveido pogas - jābūt pāra skaitlim
btn0=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn0,0)) #sāk no 0, jo sasaistās ar saraksta elementu indeksāciju
btn1=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn1,1))
btn2=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn2,2))
btn3=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn3,3))
btn4=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn4,4))
btn5=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn5,5))
btn6=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn6,6))
btn7=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn7,7))
btn8=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn8,8))
btn9=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn9,9))
btn10=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn10,10))
btn11=Button(width=200,height=300,image=bgImg,command=lambda:btnClick(btn11,11))

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
myImg6=ImageTk.PhotoImage(Image.open("6.png"))


ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5, myImg6, myImg6]#attelus ievieto masiivaa

random.shuffle(ImageList)#sajauc attelus


count=0
correctAnswers=0
answers=[]
answer_dict={}#ar iekavam nezinu
answercount=0
def btnClick(btn,number):
    global count, correctAnswers,answers,answer_dict, answercount
    if btn["image"]=="pyimage1" and count<2:#peec sisteemas nnosauc saadi
        btn["image"]=ImageList[number]
        count+=1
        answers.append(number)#bez s iespejams
        answer_dict[btn]=ImageList[number]#iespejams kantainaas
    if len(answers)==2:#ja atveras divas kartites
        if ImageList[answers[0]]==ImageList[answers[1]]:#salidzina attelus
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers+=2
            if correctAnswers==2:

                messagebox.showinfo("Vienādi attēli",'Tu uzminēji')
                correctAnswers=0
                answercount+=1
            if answercount==6:
                messagebox.showinfo("Tu uzvarēji")
                reset()


        else:
            messagebox.showinfo("Nav vienādi atteli",'Tu neuzminēji')
            for key in answer_dict:
                key["image"]="pyimage1"
        count = 0
        answers=[]
        answer_dict={}
            

    return 0


gameWindow.mainloop()
