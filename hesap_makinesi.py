from tkinter import *
import keyboard
import continuous_threading as ct


pencere = Tk()
pencere.title("Hesap Makinesi - bcelik32")
pencere.geometry('365x445')
pencere.resizable(width=False, height=False)

fun_accept=True

ekranstr=""
def eksikoy():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        ekrancek+="-"
        ekran.delete(0, END)
        ekran.insert(0,ekrancek)

    
def artıkoy():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        ekrancek+="+"
        ekran.delete(0, END)
        ekran.insert(0,ekrancek)  

def bolmekoy():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        ekrancek+="/"
        ekran.delete(0, END)
        ekran.insert(0,ekrancek)
    
def carpikoy():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        ekrancek+="*"
        ekran.delete(0, END)
        ekran.insert(0,ekrancek)

def birkoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="1"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def ikikoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="2"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def uckoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="3"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)    
    
def dortkoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="4"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek) 
    
def beskoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="5"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)
    
def altikoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="6"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def yedikoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="7"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def sekizkoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="8"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def dokuzkoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="9"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)

def sifirkoy():
    global ekranstr
    ekrancek=ekran.get()
    ekrancek+="0"
    ekran.delete(0, END)
    ekran.insert(0,ekrancek)
    
def virgulkoy():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        ekrancek+="."
        ekran.delete(0, END)
        ekran.insert(0,ekrancek)

def sifirla():
    global ekranstr
    ekran.delete(0, END)
    ekranstr=""


def sonucbul():
    if fun_accept:
        global ekranstr
        ekrancek=ekran.get()
        sonucstr=eval(ekrancek)
        ekran.delete(0, END)
        ekran.insert(0,sonucstr)
        print(sonucstr)      

def sil():
    global ekranstr
    ekrancek=ekran.get()
    ekranstr = ekrancek[:-1]
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

def hata_koruma():
    ekrancek=ekran.get()
    if not(ekrancek==""):
        global fun_accept
        if not(ekrancek[-1]==".") and not(ekrancek[-1]=="*") and not(ekrancek[-1]=="/") and not(ekrancek[-1]=="+") and not(ekrancek[-1]=="-"):
            fun_accept=True
            sonuc.configure(state="normal")
            cikarmabuton.configure(state="normal")
            toplamabuton.configure(state="normal")
            carpmabuton.configure(state="normal")
            bolmeabuton.configure(state="normal")
            virgul.configure(state="normal")

        else:
            fun_accept=False
            sonuc.configure(state="disabled")
            cikarmabuton.configure(state="disabled")
            toplamabuton.configure(state="disabled")
            carpmabuton.configure(state="disabled")
            bolmeabuton.configure(state="disabled")
            virgul.configure(state="disabled")

t1 = ct.PeriodicThread(0.1,hata_koruma) # readSerial fonksiyonunu periyodik olarak çalıştır

t1.start()
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
keyboard.add_hotkey("Slash", bolmekoy)
keyboard.add_hotkey("c", sifirla)
keyboard.add_hotkey("BackSpace", sil)
keyboard.add_hotkey(",", virgulkoy)


mainloop()