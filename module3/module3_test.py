# Soru 1: Asagidaki fonskiyonu 2 parametre alacak ve
# üstel sonucu return edecek bicimde doldurun
def my_exponents(a, b):
    return a ** b


print(my_exponents(4, 7))

print(50 * '~')

"""
Soru 2: Asagidaki fonskiyonu 2 parametre alacak ve 
üstel sonucu return edecek bicimde ve ** yerine 
for döngüsü ile hesaplayacak bicimde olusturun
"""


def my_2exponents(a, b):
    result = 1
    if b < 1:
        return result
    else:
        for kuvvet in range(1, b + 1):
            result = result * a
        return result


print(my_2exponents(5, 3))

print(50 * '~')

"""
.sort() komutu listeyi kücükten büyüge siralar
------------
Soru 3: Asagidaki fonskiyonu 1 parametre alacak (sadece
sayilardan olusan liste tipinde) ve en büyük iki sayiyi
döndürecek bicimde olusturun
"""


def listedeki_en_buyuk_iki_sayi(liste):
    liste.sort()
    return liste[-1], liste[-2]


deneme = [1, 5, 10, 2, 6]
print(listedeki_en_buyuk_iki_sayi(deneme))
print(50 * '~')

"""
Map, Filter ve Lambda Uygulamalari
Soru 4: Asagidaki fonskiyonu 1 parametre alacak (liste tipinde) 
ve sadece str tipindeki degerleri filter 
ve lambda ifadelerini kullanarak filtreleyecek bicimde olusturun
"""


def str_filtrele(liste):
    sonuc = []

    for x in liste:
        if type(x) == str:
            sonuc.append(x)
        else:
            pass
    return sonuc


print(str_filtrele([1, 2, 3, 5, 'abc', 'a', True]))
print(50 * '~')


def str_filtrele_v2(liste):
    return [*filter(lambda x: x if type(x) == str else None, liste)]


print(str_filtrele_v2([1, 2, 3, 5, 'abc', 'a', True]))

print(50 * '~')
"""
Soru 5: Asagidaki fonskiyonu 1 parametre alacak 
(sadece sayi iceren liste tipinde) 
ve map ve lambda ifadelerini kullanarak 6 sifir atacak bicimde olusturun
"""


def paradan_alti_sifir_at(liste):
    sonuc = []
    for x in liste:
        sonuc.append(int(x / 1000000))

    return sonuc


print(paradan_alti_sifir_at([1000000, 90000000, 15000000]))
print(50 * '~')


def paradan_alti_sifir_at_v2(liste):
    return [*map(lambda x: int(x / 1000000), liste)]


print(paradan_alti_sifir_at_v2([1000000, 90000000, 15000000]))

print(50 * '~')

"""
Kullanici Girdisi Uygulamasi
Soru 6: Asagidaki fonskiyonu input komutu ile kullanicidan saat 
ve dakika alacak bicimde olusuturun.
"""


def zaman_verisi_al():
    saat = input("Saat giriniz:")
    if saat.isdigit():
        saat = int(saat)
        if (saat >= 0) and (saat < 24):
            dakika = input('Dakika giriniz:')
            if dakika.isdigit():
                dakika = int(dakika)
                if (dakika >= 0) and (dakika < 60):
                    return 'Giris yapilan zaman {}:{}'.format(saat, dakika)
                else:
                    return 'Girilen dakika araligi yanlis'
            else:
                return 'Girilen dakika yanlis veri tipinde'
        else:
            return 'Girilen saat araligi yanlis'
    else:
        return 'Girilen saat yanlis veri tipinde'

print(zaman_verisi_al())
