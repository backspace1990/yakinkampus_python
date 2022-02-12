class Flight():
    airfly = "THY"


flight = Flight()

print(flight.airfly + " Turkish")


class Flight1():
    company = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika sürecektir".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure)


flight1 = Flight1('TK123', 'IST', 'ANK', 60, 300, 50)
print(flight1.anons_yap())