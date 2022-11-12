from tkinter import *

ossze = False
kivon = False
szor = False
oszt = False
muvelet = 0
   

def nulla_button():screen.insert("end","0")

def egy_button():screen.insert("end","1")

def ketto_button():screen.insert("end","2")

def harom_button():screen.insert("end","3")

def negy_button():screen.insert("end","4")

def ot_button():screen.insert("end","5")

def hat_button():screen.insert("end","6")

def het_button():screen.insert("end","7")
      
def nyolc_button():screen.insert("end","8")

def kilenc_button():screen.insert("end","9")


def plusz_button():
    global ossze, var1
    var1=int(screen.get())
    screen.delete(0,END)
    eredmeny.insert(0, str(var1) + " + ")
    ossze=True

def minusz_button():
    global var1, kivon
    var1=int(screen.get())
    screen.delete(0,END)
    eredmeny.insert(0, str(var1) + " - ")
    kivon=True


def szorzas_button():
    global var1, szor
    var1=int(screen.get())
    screen.delete(0,END)
    eredmeny.insert(0, str(var1) + " * ")
    szor=True


def osztas_button():
    global var1, oszt
    var1=int(screen.get())
    screen.delete(0,END)
    eredmeny.insert(0, str(var1) + " / ")
    oszt=True



def egyenlo_button(): 
    global muvelet
    if muvelet == 0:    
        global var2
        var2=int(screen.get())
        if ossze==True:
            eredmeny.insert(END, str(var2) + " = " + str(var1+var2))
            muvelet += 1
        elif kivon == True:
            eredmeny.insert(END, str(var2) + " = " + str(var1-var2))
            muvelet += 1
        elif szor == True:
            eredmeny.insert(END, str(var2) + " = " + str(var1*var2))
            muvelet += 1
        elif oszt == True:
            eredmeny.insert(END, str(var2) + " = " + str(round(var1/var2, 5)))
            muvelet += 1 
    elif muvelet == 1: #Diasble Button function 
        if egyenlo["state"] == "normal":
            egyenlo["state"] = "disabled"
        else:
            egyenlo["state"] = "normal"



def c_button():
    screen.delete(0, END)
    eredmeny.delete(0,END)
    global var1, ossze, var2
    var1=0
    var2=0
    ossze=False



w=Tk()
w.geometry('310x310')
w.resizable(width=False,height=False)

w.grid_columnconfigure(0, weight=1)
w.grid_columnconfigure(1, weight=1)
w.grid_columnconfigure(2, weight=1)
w.grid_columnconfigure(3, weight=1)

screen=Entry(w, width=50, font=30)
screen.grid(row=0, columnspan=4, ipady=10)

eredmeny=Entry(w,width=50, font=30)
eredmeny.grid(row=1, columnspan=4,ipady=10)
het=Button(w,width=10, height=3, text="7", command=het_button)
het.grid(row=2, column=0)
nyolc=Button(w,width=10, height=3, text="8", command=nyolc_button)
nyolc.grid(row=2, column=1)
kilenc=Button(w,width=10, height=3, text="9", command=kilenc_button)
kilenc.grid(row=2, column=2)
osszeadas=Button(w,width=10, height=3, text="+", command=plusz_button)
osszeadas.grid(row=2, column=3)
negy=Button(w,width=10, height=3, text="4", command=negy_button)
negy.grid(row=3, column=0)
ot=Button(w,width=10, height=3, text="5", command=ot_button)
ot.grid(row=3, column=1)
hat=Button(w,width=10, height=3, text="6", command=hat_button)
hat.grid(row=3, column=2)
minusz=Button(w,width=10, height=3, text="-", command=minusz_button)
minusz.grid(row=3, column=3)
egy=Button(w,width=10, height=3, text="1", command=egy_button)
egy.grid(row=4, column=0)
ketto=Button(w,width=10, height=3, text="2", command=ketto_button)
ketto.grid(row=4, column=1)
harom=Button(w,width=10, height=3, text="3", command=harom_button)
harom.grid(row=4, column=2)
szorzas=Button(w,width=10, height=3, text="×", command=szorzas_button)
szorzas.grid(row=4, column=3)
c=Button(w,width=10, height=3, text="C", command=c_button)
c.grid(row=5, column=0)
nulla=Button(w,width=10, height=3, text="0", command=nulla_button)
nulla.grid(row=5, column=1)
egyenlo=Button(w,width=10, height=3, text="=", command=egyenlo_button)
egyenlo.grid(row=5, column=2)
szazalek=Button(w,width=10, height=3, text="/", command=osztas_button)
szazalek.grid(row=5, column=3)


w.mainloop()