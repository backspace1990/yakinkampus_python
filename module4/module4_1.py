# Dunder Method'lar (Double Under Score)
class Flight1():
    company = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def __repr__(self):
        return f"{self.kod} sefer sayili ucus, sistemde olusturulmustur.."

    def anons_yap(self):
        return print(f"{self.kod} sefer sayili {self.kalkis}-{self.varis} ucusumuz {self.sure} dakika sürecektir")

    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu

    def bilet_satis(self, bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print('{} adet bilet satilmistir, kalan koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()))
        else:
            print('Islem gerceklestirilemedi. Yetersiz koltuk sayisi..')

    def bilet_iptal(self, bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print('{} adet bilet iptal edilmistir, güncel koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()))
        else:
            print('Islem gerceklestirilemedi. Iptal edilecek kadar yolcu yok..')


flight = Flight1('TK223', 'BODRUM', 'ANTALYA', 40, 250, 200)
print(flight)
flight.bilet_satis(30)
flight.bilet_iptal(230)
flight.bilet_satis(300)
flight.bilet_iptal(10)
flight.anons_yap()

for i in flight.__dir__():
    print(i)

print("\nGame over")
