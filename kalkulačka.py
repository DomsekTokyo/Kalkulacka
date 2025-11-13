import math
from tkinter import *
okno = Tk()

okno.title("Kalkulačka")
okno.iconbitmap("ikonka.ico")
okno.geometry("550x660+500+300")
okno.resizable(False,False)
okno.config(bg = "#006d00")
main_font = ("Helvetica",20)
number_font = ("helvetica",30)


frame1 = Frame(okno, bg = "#006d00")
frame1.pack()
frame2 = Frame(okno, bg = "#426d01")
frame2.pack()


entry = Entry(frame1, width=23, font=("Helvetica", 30), background="#4C5958")
entry.config(state="readonly")
entry.grid(column=0, row=0, pady = 20)

class Tlac:
    po = False
    def __init__(self, text2, souradnicex, souradnicey, okn):
        self.default_bg = "#94f567"
        self.hover_bg = "#94bf67"
        self.tlacitko = Button(okn,text= text2, relief="sunken", height=1,width=3,font=("Arial",40), background= "#94f567", activebackground="#94bf67", command= lambda: self.click(text2))
        self.tlacitko.grid(row=souradnicex,column=souradnicey,padx=3,pady = 3, ipadx = 0, ipady=0)

        self.tlacitko.bind("<Enter>", self.on_enter)
        self.tlacitko.bind("<Leave>", self.on_leave)


    def on_enter(self, event):
        self.tlacitko.config(bg=self.hover_bg)

    def auto_mul(self):
        posledni = entry.get()[-1:]
        # NIKDY nepřidávej * před mocninou
        if posledni == "²":
            return
        if posledni.isdigit() or posledni == ")":
            entry.insert("end", "*")

    def on_leave(self, event):
        self.tlacitko.config(bg=self.default_bg)

    def click(self, text):
        entry.config(state="normal")
        if entry.get() == "Chyba":
            entry.delete(0, END)

        if Tlac.po and text not in ["=", "⌫", "CE", "+", "-", "×", "÷", ")", ",", ".", "x²","%","|x|"]:
            entry.delete(0, END)
            Tlac.po = False

        if Tlac.po and text in ["+", "-", "×", "÷", ",", ".", "²","%","|x|"]:
            Tlac.po = False
        if text == "π":
            self.auto_mul()
            entry.insert("end", "π")
            return
        if text == "x²":
            entry.insert("end", "²")
            return
        if text == "(":
            self.auto_mul()
            entry.insert("end", "(")
            return
        if text == "√":
            self.auto_mul()
            entry.insert("end", "√(")
            return
        if text == "|x|":
            self.auto_mul()
            entry.insert("end", "abs(")
            return
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
                if obsah.count("(") > obsah.count(")"):
                    obsah += ")" * (obsah.count("(") - obsah.count(")"))
                obsah = (obsah.replace("²", "**2")
                    .replace("×", "*")
                    .replace("÷", "/")
                    .replace(",", ".")
                    .replace("√(", "math.sqrt(")
                    .replace("π", "math.pi")
                    .replace("%", "/100"))
                vysledek = eval(obsah)
                vysledek = round(vysledek, 2)
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
    ("CE", 0, 0), ("⌫", 0, 1), ("(", 0, 2), (")", 0, 3),("π", 0,4),
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("÷",1, 3),("x²", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2,3),("√", 2, 4),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),("-", 3,3),("%",3, 4),
    (".",4,0),("0", 4, 1),("+",4,2), ("=", 4, 3),("|x|", 4,4)


]
for text,x,y in cisla:
    Tlac(text,x,y,frame2)



okno.mainloop()