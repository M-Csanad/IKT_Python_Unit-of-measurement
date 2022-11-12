from tkinter import *
root = Tk()
root.title("Main Window")
root.geometry("300x200")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.configure(background='#0c2327')

#------------- Functions -------------

def Lenght():
    global click
    rootL = Tk()
    rootL.title("Hosszúság")
    rootL.geometry("300x320")
    rootL.resizable(False, False)
    rootL.eval('tk::PlaceWindow . center')
    rootL.configure(background='#0c2327')

    int_var = IntVar()
    ent = Entry(rootL, textvariable=int_var)

    menu = StringVar(rootL)
    menu.set("Kérem válasszon")
    drop = OptionMenu(rootL, menu, "Milliméter", "Centiméter", "Méter", "Kilométer", "Yard", "Mérföld")
    drop.config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")
    drop["menu"].config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")

    click = 0
    res = [float(0), float(0), float(0), float(0), float(0), float(0)]
    def Calc(): 
        global click, lbMilli_RES, lbCenti_RES, lbMeter_RES, lbKilom_RES, lbYard_RES, lbMerf_RES   
        num = float(ent.get())
        type = menu.get()
        if click == 0:
            btnCalc.config(text="Visszaállítás")
            if type == "Milliméter":
                res[0] = num
                res[1] = num*0.1
                res[2] = num*0.001
                res[3] = num*(pow(10, -6))
                res[4] = num*0.0011
                res[5] = num*(6.214*(pow(10, -7)))
                click += 1
            elif type == "Centiméter":
                res[0] = num*10
                res[1] = num
                res[2] = num*0.01
                res[3] = num*(pow(10, -5))
                res[4] = num*0.011
                res[5] = num*(6.214*(pow(10, -6)))
        elif click == 1:
            lbMilli_RES.config(text=" ")
            lbCenti_RES.config(text=" ")
            lbMeter_RES.config(text=" ")
            lbKilom_RES.config(text=" ")
            lbYard_RES.config(text=" ")
            lbMerf_RES.config(text=" ")
            btnCalc.config(text="Számol")
            click = 0
            return
               
        
        
        lbMilli = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Milliméter: ")
        lbMilli_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[0])
        lbCenti = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Centiméter: ")
        lbCenti_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[1])
        lbMeter = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Méter: ")
        lbMeter_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[2])
        lbKilom = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Kilométer: ")
        lbKilom_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[3])
        lbYard = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Yard: ")
        lbYard_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[4])
        lbMerf = Label(rootL, bg="#0c2327", fg="#72c4d4", text="Mérföld: ")
        lbMerf_RES = Label(rootL, bg="#0c2327", fg="#72c4d4", text=res[5])

        lbMilli.grid(row=1, column=0, sticky=W, padx=2, pady=5)
        lbMilli_RES.grid(row=1, column=1, sticky=E, padx=2, pady=5)
        lbCenti.grid(row=2, column=0, sticky=W, padx=2, pady=5)
        lbCenti_RES.grid(row=2, column=1, sticky=E, padx=2, pady=5)
        lbMeter.grid(row=3, column=0, sticky=W, padx=2, pady=5)
        lbMeter_RES.grid(row=3, column=1, sticky=E, padx=2, pady=5)
        lbKilom.grid(row=4, column=0, sticky=W, padx=2, pady=5)
        lbKilom_RES.grid(row=4, column=1, sticky=E, padx=2, pady=5)
        lbYard.grid(row=5, column=0, sticky=W, padx=2, pady=5)
        lbYard_RES.grid(row=5, column=1, sticky=E, padx=2, pady=5)
        lbMerf.grid(row=6, column=0, sticky=W, padx=2, pady=5)
        lbMerf_RES.grid(row=6, column=1, sticky=E, padx=2, pady=5)
    
    btnCalc = Button(rootL, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Számol", command=Calc)
    btnExit = Button(rootL, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=rootL.destroy)

    ent.grid(row=0, column=0, sticky=W, padx=2, pady=5)
    drop.grid(row=0, column=1, sticky=E, padx=2, pady=5) 
    btnCalc.grid(row=7, column=0, columnspan=2, sticky=EW, padx=2, pady=5)
    btnExit.grid(row=8, column=0, columnspan=2, sticky=EW, padx=2, pady=5)


def Vol():
    rootV = Tk()
    rootV.title("Térfogat")
    rootV.geometry("300x200")
    rootV.resizable(False, False)
    rootV.eval('tk::PlaceWindow . center')
    rootV.configure(background='#0c2327')

    str_var = StringVar()
    ent = Entry(rootV, textvariable=str_var)

    menu = StringVar(rootV)
    menu.set("Kérem válasszon")
    drop = OptionMenu(rootV, menu, "Milliliter", "Centiliter", "Deciliter", "Liter", "Köbmilli", "Köbcenti", "Köbdeci", "Köbméter")
    drop.config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")
    drop["menu"].config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")

    def Calc():
        None

    btnCalc = Button(rootV, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Számol", command=Calc)
    btnExit = Button(rootV, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=rootV.destroy)

    ent.grid(row=0, column=0, sticky=W, padx=2, pady=5)
    drop.grid(row=0, column=1, sticky=E, padx=2, pady=5)    
    btnCalc.grid(row=1, column=0, columnspan=2, sticky=EW, padx=2, pady=5)
    btnExit.grid(row=2, column=0, columnspan=2, sticky=EW, padx=2, pady=5)


def Weight():
    rootW = Tk()
    rootW.title("Tömeg")
    rootW.geometry("300x200")
    rootW.resizable(False, False)
    rootW.eval('tk::PlaceWindow . center')
    rootW.configure(background='#0c2327')

    str_var = StringVar()
    ent = Entry(rootW, textvariable=str_var)

    menu = StringVar(rootW)
    menu.set("Kérem válasszon")
    drop = OptionMenu(rootW, menu, "Gramm", "Dekagramm", "Kilogramm", "Font", "Uncia")
    drop.config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")
    drop["menu"].config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")

    def Calc():
        None

    btnCalc = Button(rootW, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Számol", command=Calc)
    btnExit = Button(rootW, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=rootW.destroy)
    
    ent.grid(row=0, column=0, sticky=W, padx=2, pady=5)
    drop.grid(row=0, column=1, sticky=E, padx=2, pady=5)
    btnCalc.grid(row=1, column=0, columnspan=2, sticky=EW, padx=2, pady=5)
    btnExit.grid(row=2, column=0, columnspan=2, sticky=EW, padx=2, pady=5)


def Time():
    
    rootT = Tk()
    rootT.title("Idő")
    rootT.geometry("300x200")
    rootT.resizable(False, False)
    rootT.eval('tk::PlaceWindow . center')
    rootT.configure(background='#0c2327')

    str_var = StringVar()
    ent = Entry(rootT, textvariable=str_var)

    menu = StringVar(rootT)
    menu.set("Kérem válasszon") 
    drop = OptionMenu(rootT, menu,  "Másodperc", "Perc", "Óra", "Nap", "Hét", "Hónap", "Év")
    drop.config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")
    drop["menu"].config(bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4")

    def Calc():
        None

    btnCalc = Button(rootT, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Számol", command=Calc)
    btnExit = Button(rootT, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=rootT.destroy)
    

    ent.grid(row=0, column=0, sticky=W, padx=2, pady=5)
    drop.grid(row=0, column=1, sticky=E, padx=2, pady=5)
    btnCalc.grid(row=1, column=0, columnspan=2, sticky=EW, padx=2, pady=5)
    btnExit.grid(row=2, column=0, columnspan=2, sticky=EW, padx=2, pady=5)

#------------------------------------------------------------






#------------- Root elements and their properties -------------

lb = Label(root, bg="#0c2327", fg="#72c4d4", text="Mértékegység átváltó")
btnL = Button(root, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text='Hosszúság', command=Lenght)
btnV = Button(root, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text='Térfogat', command=Vol)
btnW = Button(root, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text='Tömeg', command=Weight)
btnT = Button(root, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text='Idő', command=Time)
btnExit = Button(root, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=root.quit)

lb.grid(row=0, column=0, columnspan=2, sticky=N, pady=10)
btnL.grid(row=1, column=0, sticky=W, padx=2, pady=5)
btnV.grid(row=1, column=1, sticky=E, padx=2, pady=5)
btnW.grid(row=2, column=0, sticky=W, padx=2, pady=5)
btnT.grid(row=2, column=1, sticky=E, padx=2, pady=5)
btnExit.grid(row=3, column=0, columnspan=2, sticky=EW, padx=2, pady=5)

#------------------------------------------------------------

root.mainloop()




