import string
import random


class Jelszoobjektum():
    jelszo = ''
    jelszohossz = None
    van_szamjegy = None
    van_irasjel = None

    def __init__(self):
        self.jelszohossz = 5
        self.van_szamjegy = True
        self.van_irasjel = False

    def jelszo_alap(self):
        self.jelszo = '123456'

    def jelszogenerator(self):
        karakterlista = string.ascii_letters
        self.jelszo = ''
        if self.van_szamjegy:
            karakterlista = karakterlista + string.digits
        if self.van_irasjel:
            karakterlista = karakterlista + string.punctuation
        for _ in range(self.jelszohossz):
            self.jelszo = self.jelszo + karakterlista[random.randint(0, len(karakterlista) - 1)]

class Szemely(Jelszoobjektum):
    def __init__(self):
        super().__init__()
        self.nev = ''
        self.kor = 0
        self.email = ''
    def email_ellenrozes(sel, email):
        if '@' not in email:
            print('Nem jó az email!')

class Dolgozok(Szemely):
    def __init__(self):
        super().__init__()
        self.reszleg = ''
        self.beosztas = ''
        self.fizetes = ''

if __name__ == '__main__':
    dolg1 = Dolgozok()
    print(dolg1.nev, dolg1.kor, dolg1.email, dolg1.reszleg, dolg1.beosztas, dolg1.fizetes)
    dolg1.jelszohossz = 15
    dolg1.jelszogenerator()
    print(dolg1.jelszo)

    dolg1.email_ellenrozes(dolg1.email)



    '''pwd = Jelszoobjektum()
    pwd.van_irasjel = True
    pwd.jelszogenerator()

    print(pwd.jelszo)
    print(pwd.jelszohossz)
    print(pwd.van_szamjegy)
    print(pwd.van_irasjel)'''