import random, math



#help(random)
print(int((str(random.random() * 10))[0]))
print(50 * "*")
#help(math)
print(int((str(random.uniform(5,7) * 10))[0]))

print(50 * "*")


print(random.randint(0,10))

print(50 * "*")

print([*range(10)])

print(50 * "*")

print(random.choice([*range(10)]))
print(50 * "*")
print(random.choice(range(10)))
print(50 * "*")
print(random.sample(range(10), k = 4))
print(50 * "*")


lists = [*range(19)]
print(lists)
random.shuffle(lists)
print(lists)

###### Math modules
print(50 * "*")

#help(math)

print(math.ceil(8.3))
print(50 * "*")
print(math.floor(10.99999))
print(50 * "*")

print(math.factorial(6))

print(50 * "*")

print(math.pow(3,2))
