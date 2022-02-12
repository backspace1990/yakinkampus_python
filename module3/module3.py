def prints(argv):
    print(argv)


prints(5)
prints("Hi peoples")

prints(20 * '~')


def who_is_big(a, b):
    if a >= b:
        prints(a)
    else:
        prints(b)


who_is_big(5, 10)

prints(20 * '~')


def my_join_func(arg1="", arg2=""):
    return " ".join([arg1, arg2])


prints(my_join_func("umit", "asan"))

prints(20 * '~')


def my_big_join_func(*args):
    return " ".join(args)


prints(my_big_join_func("umit", "asan", "love", "ekaterina", "latisheva"))

prints(20 * '~')


def print_name_surname(**kwargs):
    for kw in kwargs:
        prints(my_join_func(kw, kwargs[kw]))


print_name_surname(name='Umit', last_name='Tgrandis', surname='Asan')

prints(20 * '~')


def kare_al(x):
    prints(x ** 2)


kare_al(25)

prints(20 * '~')


def kare_al2(x):
    return x ** 2


number = [*range(1, 6)]
print(number)
print([*map(kare_al2, number)])
prints(20 * '~')


def cift_sayilari_filtrele(x):
    return x if x % 2 == 0 else None


prints(cift_sayilari_filtrele(10))
prints(20 * '~')

sayilar = [*range(1, 6)]
print([*filter(cift_sayilari_filtrele, sayilar)])
prints(20 * '~')

sayilar = [*range(1, 6)]
print([*map(lambda x: x ** 2, sayilar)])
prints(20 * '~')

sayilar = [*range(1, 6)]
print([*filter(lambda x: x if x % 2 == 0 else None, sayilar)])


def eposta_kontrol():
    # umut90asan@gmail.com

    girdi = input("Gecerli bir eposta adresi giriniz:")

    while not (('.' in girdi) and ('@' in girdi)):
        print("Üzgünüm! Bu gecerli bir e-posta adresi degildir...")
        girdi = input("Gecerli bir eposta adresi giriniz:")

    else:
        print("Tebrikler! E-posta adresinizle basariyla giris yaptiniz...")


# eposta_kontrol()
prints(20 * '~')
# Try, Except ve Finally Komutlari

vatandas = {
    'AD': 'Oguz',
    'TC_NO': 123123
}

try:
    vatandas['PASS_NO']
except IndexError:
    print('Indexlemeye calistiginiz eleman listenin disinda')
except KeyError:
    print('Aranan dictionaryde verilen anahtar degeri mevcut degil')
except:
    print('kod duzgun calismiyor')

prints(20 * '~')


def tam_sayiya_cevir():
    girdi = input("Bir ondalik sayi giriniz:")

    status = ''

    try:
        girdi = float(girdi)
        print("Yuvarlama isleminin sonucu: {}".format(round(girdi)))
        status = 'basarili'
    except:
        print("{} girdisi ondalik tipe cevrilemiyor".format(girdi))
        status = 'basarisiz'
    finally:
        print('Tam sayiya cevirme islemi {} olarak tamamlandi!'.format(status))


#tam_sayiya_cevir()

prints(20 * '~')

__name__ == '__main__'
