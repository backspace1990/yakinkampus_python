import os
import time

print(os.getcwd())
print(os.listdir())
print(100 * "*")

for i in os.listdir('/Users/umitasan/'):
    print(i)

print(100 * "*")

os.chdir('/Users/umitasan/') #chdir - change directory bunu yazinca listdir() -- > chdir("/Users/umitasan") ayni oluyor


for i in os.listdir():
    print(i)
print(100 * "*")

os.chdir('/Users/umitasan/PycharmProjects/yakinkampus_python/module5') #chdir - change directory bunu yazinca listdir() -- > chdir("/Users/umitasan") ayni oluyor


for i in os.listdir():
    print(i)

i = 1

while True:
    if i == 5:
        break
    virus = 'de'
    uzanti = '.txt'
    text = '/Users/umitasan/PycharmProjects/yakinkampus_python/module5/'
    text = text + virus * i + uzanti
    os.mkdir(text)
    time.sleep(1)
    i +=1


time.sleep(5)

i = 1
while True:
    if i == 5:
        break
    virus = 'de'
    uzanti = '.txt'
    text = '/Users/umitasan/PycharmProjects/yakinkampus_python/module5/'
    text = text + virus * i + uzanti
    os.rmdir(text)
    i += 1