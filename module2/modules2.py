# if - elif - else

weather = "Winter"

if weather == "winter" or weather == "Winter":
    print("Take your scarf!")
elif weather == "" or weather == None:
    print(f"Not weather values{weather}")
else:
    print("bug bu big")

# for Loops
people_comments =  ["Ismail Aydemir", "Uygar Aydin", "Naz Yagcioglu","Ferhat Ibrik","Ulas Acil", "Bilal Kurucay"]

for name in people_comments:
    print(name)

numbers_users = 0;
for name in people_comments:
    numbers_users += 1
    print(f"Number {numbers_users} he is {name}")
    #print("Number {} he is {}".format(numbers_users,name))

numbers_users = 0
for name in people_comments:
    numbers_users += 1
    print(f"Number {numbers_users} his name is {name.split()[0]} surnames : {name.split()[1]}")


tup1 = (1, 3, 5, 7)
for number in tup1:
    print(number + 1)

lists = [[0,1],[2,3],[4,5]]
for a,b in lists:
    print(f"first number : {a} -- second number : {b} --- first * second = {a * b}")

users = {'ad': 'Naz', 'soyad' : 'yagci'}
for key, value in users.items():
    print(f"Key: {key} {10 * '*'} Value: {value}")

for key in users.keys():
    print(f"Key: {key}")
for value in users.values():
    print(f"Values: {value}")

# While loops
x = 6
number = 1
while x > 1:
    number = number * x
    x-=1
print(number)

print(50 * '~')


for sayi in range(1,6):
    if sayi%2 == 0:
        pass
    else:
        print(sayi)
print(50 * '~')
for sayi in range(1,6):
    if sayi%2 == 0:
        continue
    print(sayi)

print(50 * '~')
index = 0
harfler = ['a','b','c','d','e']
for harf in harfler:
    index += 1
    if harf == 'c':
        print("{} harfi {} konumda ve {}. indexte!".format(harf, index, index-1))
        break

for harf in enumerate(harfler):
    print(harf)

for index, value in enumerate(harfler):
    print(index, value)

country = ['TR', 'FR', 'DE']
lists1 = [1,2,3]

for contr in zip(lists1, country):
    print(contr[1], contr, contr[1] + 'iye')