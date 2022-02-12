kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End']
}
print("Soru 1: Ferhat Ibrik Kullanicisinin uzmanlik alanlarini döndür")
# Soru 1: Ferhat Ibrik Kullanicisinin uzmanlik alanlarini döndür
print(kullanici1.get('uzmanlik'))
print(kullanici1['uzmanlik'][0])

print(50 * '~')
print(" Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür")
kullanici_listesi = [kullanici1, kullanici2, kullanici3]

# Soru 2: Front-end alanindaki uzmanlarin isimlerini döndür
for kullanici in kullanici_listesi:
    if 'Front-End' in kullanici.get('uzmanlik'):
        print(kullanici.get('ad'))

print(50 * '~')
print("Soru 3: Mesut kullanicisi Yazilim ögrendi, bilgileri güncelle!")
# Soru 3: Mesut kullanicisi Yazilim ögrendi, bilgileri güncelle!
kullanici3['uzmanlik'].append('Yazilim')
print(kullanici_listesi)

print(50 * '~')
print("Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)")

# Soru 4: 1den fazla uzmanlik alani olan kullanicilari döndür (Hint: length)

for kullanici in kullanici_listesi:
    if len(kullanici['uzmanlik']) > 1:
        print(kullanici)

print(50 * '~')
print("Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?")

kullanici_yaslari_listesi = [22, 34, 32]
# Soru 5: zip kullanarak iki listeyi birlestir ve yasi 30'dan az olan kullanicilar kimler?

for kullanici, yas in zip(kullanici_listesi, kullanici_yaslari_listesi):
    if yas < 30:
        print(kullanici)

print(50 * '~')
print("Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!")

# Soru 6: deger isimli degiskene atanan sayinin asal olup olmadigini söyle!
# Hint Asal sayi: kendinden ve 1'den baska böleni olmayan sayilar örnek 2,3,5,7

deger = 7
x=deger-1
while x>1:
    if deger%x==0:
        print('{} sayisi asal degil!'.format(deger))
        break
    else:
        x-=1
else:
    print('{} sayisi asaldir!'.format(deger))