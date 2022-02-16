import datetime
import time
from datetime import date

print(date.today())
print(50 * "*")

dun = date(2020, 10, 20)
print(dun)
print(50 * "*")

bugun = date.today()

print(bugun - dun)
print(50 * "*")

yarin = bugun + datetime.timedelta(days=1)
print(yarin)
print(50 * "*")
zaman_araligi = yarin - bugun
print(zaman_araligi.days)

print(50 * "*")

print(bugun.__getattribute__('month'))

print(50 * "*")
print(date.isocalendar(bugun))
print(date.isocalendar(bugun)[0])
print(50 * "*")
print(date.weekday(bugun))
print(50 * "*")
print(date.ctime(bugun))

print(50 * "*")
bremya = datetime.datetime
print(bremya.today())
print(50 * "*")
print(time.ctime().split())
print(50 * "*")
print(time.time())
print(50 * "*")
baslangic_zamani = time.time()
time.sleep(5)
bitis_zamani = time.time()
print(f"{baslangic_zamani} saniyede basladim. 5 saniye uyudum.\nuyanis zamanim : {bitis_zamani} \naradaki fark {bitis_zamani - baslangic_zamani} \nyuvarlanmis hali {round(bitis_zamani - baslangic_zamani)}")
print(50 * "*")

