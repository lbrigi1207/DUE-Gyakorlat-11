from tkinter import *
import objektumok

class Ember():
    nev = ''
    kor = 0
    diak = ''

    def __init__(self): #alapérték beállítható
        self.diak = 'középfokú'

    def info(self):
        print(self.nev, self.kor, self.diak)

class Hallgato(Ember):
    neptunkod = ''

    def __init__(self):
        super().__init__() #örökölt osztály init metódusának lefuttatására
        self.neptunkod = 'XXXX'

def info():
    hallgato_cimke = Label(ablak, text='Hallgató neve')
    hallgato_cimke.pack()

ablak = Tk()

menusor = Menu(ablak)
home = Menu(ablak)
info = Menu(menusor)
info.add_command(label='Információ', command=info)
info.add_command(label='Kilépés', command=ablak.destroy)
info.add_cascade(label='Home', menu=home)

ablak.config(menu=menusor)
ablak.mainloop()

valaki = Hallgato()

valaki.nev = 'Jenő'
valaki.kor = 50
valaki.neptunkod = 'ABCD45'

valaki.info()
print(valaki.neptunkod)
