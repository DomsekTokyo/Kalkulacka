from distutils.command.clean import clean
from tkinter import *
okno = Tk()

okno.title("Kalkulačka")
#okno.iconbitmap("ikonka.ico")
okno.geometry("500x680+500+300")
okno.resizable(False,False)
okno.config(bg = "#4C5958")
main_font = ("Helvetice",20)
number_font = ("helvetica",30)


frame1 = Frame(okno, bg = "#4C5958")
frame1.pack()
frame2 = Frame(okno, bg = "#4C5958")
frame2.pack()


entry = Entry(frame1, width=20, font=("Helvetica", 30), background="#4C5958")
entry.config(state="readonly")
entry.grid(column=0, row=0, pady = 20)

class Tlac:
    po = False
    def __init__(self, text2, souradnicex, souradnicey, okn):
        self.default_bg = "#4C5958"
        self.hover_bg = "#5C6C68"
        self.tlacitko = Button(okn,text= text2, relief="sunken", height=1,width=3,font=("Arial",40), background= "#4C5958", activebackground="#3A5958", command= lambda: self.click(text2))
        self.tlacitko.grid(row=souradnicex,column=souradnicey,padx=3,pady = 3, ipadx = 0, ipady=0)

        self.tlacitko.bind("<Enter>", self.on_enter)
        self.tlacitko.bind("<Leave>", self.on_leave)


    def on_enter(self, event):
        self.tlacitko.config(bg=self.hover_bg)


    def on_leave(self, event):
        self.tlacitko.config(bg=self.default_bg)

    def click(self, text):
        entry.config(state="normal")
        if entry.get() == "Chyba":
            entry.delete(0, END)

        if Tlac.po and text not in ["=", "⌫", "CE", "+", "-", "×", "÷", ")", ","]:
            entry.delete(0, END)
            Tlac.po = False

        if Tlac.po and text in ["+", "-", "×", "÷", ","]:
            Tlac.po = False

        if text == "CE":

            entry.delete(0, "end")
            entry.config(state="readonly")
        elif text == "⌫":

            entry.delete(len(entry.get()) - 1, "end")
            entry.config(state="readonly")
    #wtf
        elif text == "=":

            try:
                obsah = entry.get()
                obsah = obsah.replace("×","*").replace("÷","/").replace(",",".")
                vysledek = eval(obsah)
                entry.delete(0, END)

                entry.insert(0, str(vysledek))
                Tlac.po = True

            except:
                entry.delete(0,END)

                entry.insert(0, str("Chyba"))

        else:
            entry.insert("end", text)
        entry.config(state="readonly")














cisla = [
    ("CE", 0, 0), ("⌫", 0, 1), ("(", 0, 2), (")", 0, 3),
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("÷",1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2,3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),("-", 3,3),
    (".",4,0),("0", 4, 1),("+",4,2), ("=", 4, 3)

]
for text,x,y in cisla:
    Tlac(text,x,y,frame2)



okno.mainloop()