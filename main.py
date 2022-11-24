# jelszógenerátor
from tkinter import *
import objektumok



def jelszokiiras():
    try:
        p.jelszohossz = int(hossz.get())
    except:
        jelszo_ertek['state'] = NORMAL
        jelszo_ertek.delete(1.0, END)
        jelszo_ertek.insert(END, 'Hiba! Nem szám!')
        jelszo_ertek.grid(row=1, column=2)
        jelszo_ertek['state'] = DISABLED
        hibaablak = Toplevel(ablak)
        hibaablak.geometry('200x200')
        hibaablak.title('Hibajelzés')
        hibauzenet = Label(hibaablak, text='A jelszó hossza csak számjegy lehet', fg='red', pady=15)
        hibauzenet.grid(row=0)
        ok = Button(hibaablak, text='OK', command=hibaablak.destroy, width=10, height=3)
        ok.grid(row=1, sticky=E)
        hibaablak.mainloop()
    else:
        p.van_szamjegy = szamjegy.get()
        p.van_irasjel = irasjel.get()
        p.jelszogenerator()
        jelszo_ertek['state'] = NORMAL
        jelszo_ertek.delete(1.0, END)
        jelszo_ertek.insert(END, p.jelszo)
        jelszo_ertek.grid(row=1, column=2)
        jelszo_ertek['state'] = DISABLED


p = objektumok.Dolgozok


ablak = Tk()
ablak.title('Jelszógenerálás')
ablak.minsize(width=200, height=100)

cim = Label(ablak, text='Jelszókezelés')
cim.grid(row=0, column=1)

jelszo_cimke = Label(ablak, text='A jelszó: ', fg='red')
jelszo_cimke.grid(row=1, column=0, sticky=E)

jelszo_ertek = Text(ablak, height=1, width=15, state=DISABLED)
jelszo_ertek.grid(row=1, column=2)

jelszo_hossza = Label(ablak, text='A jelszó hossza:')
jelszo_hossza.grid(row=2, column=0)

hossz = Entry(ablak, width=3)
hossz.insert(0, '8')
hossz.grid(row=2, column=2, sticky=W)

szamjegy = BooleanVar()
hossz_pipa = Checkbutton(ablak, text="Kell számjegy?", variable=szamjegy)
hossz_pipa.grid(row=3, column=0)

irasjel = BooleanVar()
irasjel_pipa = Checkbutton(ablak, text='Kell írásjel?', variable=irasjel)
irasjel_pipa.grid(row=3, column=1)

lezaro_gomb = Button(ablak, text='Lezárás', command=ablak.destroy)
lezaro_gomb.grid(row=5, column=2)

jelszo_gomb = Button(ablak, text='Generálás', command=jelszokiiras)
jelszo_gomb.grid(row=5, column=0, columnspan=2)

mainloop()