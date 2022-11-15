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
                click += 1
                
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
    
    global click
    rootT = Tk()
    rootT.title("Idő")
    rootT.geometry("300x400")
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

    click = 0
    tim = [float(0), float(0), float(0), float(0), float(0), float(0), float(0)]
    def Calc():
        global click, lbMasodp_TIM, lbPerc_TIM, lbOra_TIM, lbNap_TIM, lbHet_TIM, lbHonap_TIM, lbEv_TIM   
        num = float(ent.get())
        type = menu.get()
        if click == 0:
            btnCalc.config(text="Visszaállítás")
            if type == "Nap":
                tim[3] = num
                tim[0] = num*86400
                tim[1] = num*1440
                tim[2] = num*24
                tim[4] = num*0.1429
                tim[5] = num*0.0323
                tim[6] = num*(2.7*(pow(10,-3)))
                click += 1
            elif type == "Perc":
                tim[0] = num*60
                tim[1] = num
                tim[2] = num*0.0167
                tim[3] = num*(7*(pow(10,-4)))
                tim[4] = num*(pow(10,-4))
                tim[5] = num*(2.2401*(pow(10,-5)))
                tim[6] = num*(1.9026*(pow(10,-6)))
                click += 1
            elif type == "Másodperc":
                tim[0] = num
                tim[1] = num*0.0167
                tim[2] = num*(3*(pow(10,-4)))
                tim[3] = num*(1.1574*(pow(10,-5)))
                tim[4] = num*(1.6534*(pow(10,-4)))
                tim[5] = num*(3.7336*(pow(10,-7)))
                tim[6] = num*(3.171*(pow(10,-8)))
                click += 1
            elif type == "Óra":
                tim[0] = num*3600
                tim[1] = num*60
                tim[2] = num
                tim[3] = num*0.0417
                tim[4] = num*0.006
                tim[5] = num*0.0013
                tim[6] = num*(pow(10,-4))
                click += 1
            elif type == "Hét":
                tim[0] = num*604800
                tim[1] = num*10080
                tim[2] = num*168
                tim[3] = num*7
                tim[4] = num
                tim[5] = num*0.2258
                tim[6] = num*0.0192
                click += 1
            elif type == "Hónap":
                tim[0] = num*2678400
                tim[1] = num*44640
                tim[2] = num*744
                tim[3] = num*31
                tim[4] = num*4.4286
                tim[5] = num
                tim[6] = num*0.0849
                click += 1
            elif type == "Év":
                tim[0] = num*31536000
                tim[1] = num*525600
                tim[2] = num*8760
                tim[3] = num*365
                tim[4] = num*52,1429
                tim[5] = num*11,7742
                tim[6] = num
                click += 1
                
        elif click == 1:
            lbMasodp_TIM.config(text=" ")
            lbPerc_TIM.config(text=" ")
            lbOra_TIM.config(text=" ")
            lbNap_TIM.config(text=" ")
            lbHet_TIM.config(text=" ")
            lbHonap_TIM.config(text=" ")
            lbEv_TIM.config(text=" ")
            btnCalc.config(text="Számol")
            click = 0
            return

        lbMasodp = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Másodperc: ")
        lbMasodp_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[0])
        lbPerc = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Perc: ")
        lbPerc_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[1])
        lbOra = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Óra: ")
        lbOra_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[2])
        lbNap = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Nap: ")
        lbNap_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[3])
        lbHet = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Hét: ")
        lbHet_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[4])
        lbHonap = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Hónap: ")
        lbHonap_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[5])
        lbEv = Label(rootT, bg="#0c2327", fg="#72c4d4", text="Év: ")
        lbEv_TIM = Label(rootT, bg="#0c2327", fg="#72c4d4", text=tim[6])

        lbMasodp.grid(row=1, column=0, sticky=W, padx=2, pady=5)
        lbMasodp_TIM.grid(row=1, column=1, sticky=E, padx=2, pady=5)
        lbPerc.grid(row=2, column=0, sticky=W, padx=2, pady=5)
        lbPerc_TIM.grid(row=2, column=1, sticky=E, padx=2, pady=5)
        lbOra.grid(row=3, column=0, sticky=W, padx=2, pady=5)
        lbOra_TIM.grid(row=3, column=1, sticky=E, padx=2, pady=5)
        lbNap.grid(row=4, column=0, sticky=W, padx=2, pady=5)
        lbNap_TIM.grid(row=4, column=1, sticky=E, padx=2, pady=5)
        lbHet.grid(row=5, column=0, sticky=W, padx=2, pady=5)
        lbHet_TIM.grid(row=5, column=1, sticky=E, padx=2, pady=5)
        lbHonap.grid(row=6, column=0, sticky=W, padx=2, pady=5)
        lbHonap_TIM.grid(row=6, column=1, sticky=E, padx=2, pady=5)
        lbEv.grid(row=7, column=0, sticky=W, padx=2, pady=5)
        lbEv_TIM.grid(row=7, column=1, sticky=E, padx=2, pady=5)

    btnCalc = Button(rootT, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Számol", command=Calc)
    btnExit = Button(rootT, bg="#0c2327", fg="#72c4d4", activebackground="#153e45", activeforeground="#72c4d4", borderwidth=0, width=20, height=2, text="Exit", command=rootT.destroy)
    

    ent.grid(row=0, column=0, sticky=W, padx=2, pady=5)
    drop.grid(row=0, column=1, sticky=E, padx=2, pady=5)
    btnCalc.grid(row=8, column=0, columnspan=2, sticky=EW, padx=2, pady=5)
    btnExit.grid(row=9, column=0, columnspan=2, sticky=EW, padx=2, pady=5)

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




