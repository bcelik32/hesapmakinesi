from tkinter import *
import keyboard


pencere = Tk()
pencere.geometry('365x445')
pencere.title("Hesap Makinesi - bcelik32")

ekranstr=""

def birkoy():
    global ekranstr
    ekranstr+="1"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def ikikoy():
    global ekranstr
    ekranstr+="2"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def artıkoy():
    global ekranstr
    ekranstr+="+"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)  
    
def eksikoy():
    global ekranstr
    ekranstr+="-"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)
    
def carpikoy():
    global ekranstr
    ekranstr+="x"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)            
    
def bolmekoy():
    global ekranstr
    ekranstr+="÷"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)     
    
def uckoy():
    global ekranstr
    ekranstr+="3"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)    
    
def dortkoy():
    global ekranstr
    ekranstr+="4"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr) 
    
def beskoy():
    global ekranstr
    ekranstr+="5"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)
    
def altikoy():
    global ekranstr
    ekranstr+="6"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def yedikoy():
    global ekranstr
    ekranstr+="7"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def sekizkoy():
    global ekranstr
    ekranstr+="8"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def dokuzkoy():
    global ekranstr
    ekranstr+="9"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def sifirkoy():
    global ekranstr
    ekranstr+="0"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)

def bolmekoy():
    global ekranstr
    ekranstr+="÷"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)
    
def carpikoy():
    global ekranstr
    ekranstr+="*"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr)
    
def eksikoy():
    global ekranstr
    ekranstr+="-"
    ekran.delete(0, END)
    ekran.insert(0,ekranstr) 
    
def virgulkoy():
    global ekranstr
    ekranstr+="."
    ekran.delete(0, END)
    ekran.insert(0,ekranstr) 

def sifirla():
    global ekranstr
    ekran.delete(0, END)
    ekranstr=""


def sonucbul():
    global ekranstr
    ekrancek=ekran.get()
    sonucstr=eval(ekrancek)
    ekran.delete(0, END)
    ekran.insert(0,sonucstr)       

def sil():
    global ekranstr
    ekranstr = ekranstr[:-1]
    ekran.delete(0, END)
    ekran.insert(0,ekranstr) 

ekran=Entry(pencere)
ekran.place(x=53,y=7, width=257,height=70)
ekran.config(text='Sayıları Yazınız', fg='black',font=("Vertana",35))

toplamabuton=Button(pencere)
toplamabuton.pack()
toplamabuton.place(x=275,y=355,height=85, width=85)
toplamabuton.config(text='+', bg='#C1BED9',font=("Vertana",17),command=artıkoy)

cikarmabuton=Button(pencere)
cikarmabuton.pack()
cikarmabuton.place(x=275,y=265,height=85, width=85)
cikarmabuton.config(text='-', bg='#C1BED9',font=("Vertana",17),command=eksikoy)

carpmabuton=Button(pencere)
carpmabuton.pack()
carpmabuton.place(x=275,y=175,height=85, width=85)
carpmabuton.config(text='x', bg='#C1BED9',font=("Vertana",17),command=carpikoy)

bolmeabuton=Button(pencere)
bolmeabuton.pack()
bolmeabuton.place(x=275,y=85,height=85, width=85)
bolmeabuton.config(text='÷', bg='#C1BED9',font=("Vertana",17),command=bolmekoy)

cbuton=Button(pencere)
cbuton.pack()
cbuton.place(x=5,y=7,height=70, width=42)
cbuton.config(text='C', bg='#C1BED9',font=("Vertana",17),command=sifirla)

silbuton=Button(pencere)
silbuton.pack()
silbuton.place(x=318,y=7,height=70, width=42)
silbuton.config(text='←', bg='#C1BED9',font=("Vertana",17),command=sil)

sonuc=Button(pencere)
sonuc.pack()
sonuc.place(x=185,y=355,height=85, width=85)
sonuc.config(text='=', bg='#C1BED9',font=("Vertana",17),command=sonucbul,)
pencere.bind('<Enter>', sonucbul)



bir=Button(pencere)
bir.pack()
bir.place(x=5,y=265,height=85, width=85)
bir.config(text='1', bg='#C1BED9',font=("Vertana",17), command=birkoy)

iki=Button(pencere)
iki.pack()
iki.place(x=95,y=265,height=85, width=85)
iki.config(text='2', bg='#C1BED9',font=("Vertana",17), command=ikikoy)

uc=Button(pencere)
uc.pack()
uc.place(x=185,y=265,height=85, width=85)
uc.config(text='3', bg='#C1BED9',font=("Vertana",17), command=uckoy)

dort=Button(pencere)
dort.pack()
dort.place(x=5,y=175,height=85, width=85)
dort.config(text='4', bg='#C1BED9',font=("Vertana",17), command=dortkoy)

bes=Button(pencere)
bes.pack()
bes.place(x=95,y=175,height=85, width=85)
bes.config(text='5', bg='#C1BED9',font=("Vertana",17), command=beskoy)

alti=Button(pencere)
alti.pack()
alti.place(x=185,y=175,height=85, width=85)
alti.config(text='6', bg='#C1BED9',font=("Vertana",17), command=altikoy)

yedi=Button(pencere)
yedi.pack()
yedi.place(x=5,y=85,height=85, width=85)
yedi.config(text='7', bg='#C1BED9',font=("Vertana",17), command=yedikoy)

sekiz=Button(pencere)
sekiz.pack()
sekiz.place(x=95,y=85,height=85, width=85)
sekiz.config(text='8', bg='#C1BED9',font=("Vertana",17), command=sekizkoy)


dokuz=Button(pencere)
dokuz.pack()
dokuz.place(x=185,y=85,height=85, width=85)
dokuz.config(text='9', bg='#C1BED9',font=("Vertana",17), command=dokuzkoy)

sifir=Button(pencere)
sifir.pack()
sifir.place(x=95,y=355,height=85, width=85)
sifir.config(text='0', bg='#C1BED9',font=("Vertana",17), command=sifirkoy)

virgul=Button(pencere)
virgul.pack()
virgul.place(x=5,y=355,height=85, width=85)
virgul.config(text=',', bg='#C1BED9',font=("Vertana",26), command=virgulkoy)

keyboard.add_hotkey("Return", sonucbul)
keyboard.add_hotkey("1", birkoy)
keyboard.add_hotkey("2", ikikoy)
keyboard.add_hotkey("3", uckoy)
keyboard.add_hotkey("4", dortkoy)
keyboard.add_hotkey("5", beskoy)
keyboard.add_hotkey("6", altikoy)
keyboard.add_hotkey("7", yedikoy)
keyboard.add_hotkey("8", sekizkoy)
keyboard.add_hotkey("9", dokuzkoy)
keyboard.add_hotkey("0", sifirkoy)
keyboard.add_hotkey("+", artıkoy)
keyboard.add_hotkey("-", eksikoy)
keyboard.add_hotkey("*", carpikoy)
keyboard.add_hotkey("/", bolmekoy)
keyboard.add_hotkey("c", sifirla)
keyboard.add_hotkey("BackSpace", sil)
keyboard.add_hotkey(",", virgulkoy)


mainloop()