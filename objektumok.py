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
        self.nev = 'nev'
        self.kor = 0
        self.email = 'email'

    def email_ell(self, email):
        if '@' not in email:
            print('Nem jó az email!')


class Dolgozo(Szemely):
    def __init__(self):
        super().__init__()
        self.beosztas = 'beosztas'
        self.reszleg = 'reszleg'
        self.fizetes = 0


if __name__ == '__main__':
    dolgozo1 = Dolgozo()
    print(dolgozo1.nev, dolgozo1.kor, dolgozo1.email, dolgozo1.reszleg, dolgozo1.beosztas, dolgozo1.fizetes)
    dolgozo1.jelszohossz = 10
    dolgozo1.jelszogenerator()
    print(dolgozo1.jelszo)
    dolgozo1.email_ell(dolgozo1.email)

'''    pwd = Jelszoobjektum()
    pwd.van_irasjel = True
    pwd.jelszogenerator()
    print(pwd.jelszo)
    print(pwd.jelszohossz)
    print(pwd.van_szamjegy)
    print(pwd.van_irasjel)
'''