# Inheritance (Kalitim)
class Seyahat():

    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis

    def anons(self):
        return print(f"{self.kalkis}-{self.varis} seyahatine hosgeldiniz")


class Otobus(Seyahat):

    def __init__(self, mola_duraklari, kalkis, varis):
        Seyahat.__init__(self, kalkis, varis)
        self.mola_duraklari = mola_duraklari


seyahat1 = Seyahat('ANT','BOD')
seyahat1.anons()

oto1 = Otobus(['FET', 'ALAN'], 'ANT', 'BOD')
print(oto1.mola_duraklari)
print(oto1.kalkis)
oto1.anons()


