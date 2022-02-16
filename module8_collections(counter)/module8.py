from collections import Counter
import random

lists1 = random.sample(range(10), k=5)
lists2 = random.sample(range(10), k=5)
lists3 = random.sample(range(10), k=5)
lists4 = random.sample(range(10), k=5)
lists5 = random.sample(range(10), k=5)

lists = [lists1, lists2, lists3, lists4, lists5]
lists_sum = lists1 + lists2 + lists3 + lists4 + lists5
print(lists_sum)
print(50 * "*")
for index, i in enumerate(lists):
    print(f"{index + 1}. liste : {i}")

print(50 * "*")
print(lists)

print(50 * "*")

print(Counter(lists_sum))
print(50 * "*")

print(Counter("dsabduysabdonsauigvtyfvcbxnljciuagudtgsajl;ojhfiyugvsajbdijsal;kl"))

print(50 * "*")

music = """
Yine bana gel
Yana yana yine beni sev
Yine bana gel
Yana yana yine beni sev
"""
print(music)

print(Counter(music))

print((50 * "*"))

print(Counter(music.lower().split()))

print(50 * "*")

print(Counter(music.lower().split()).most_common())
print(50 * "*")
for i in Counter(music.lower().split()).most_common():
    print(i)

print(50 * "*")
print(Counter(music.lower().split()).most_common(4))
print(Counter(music.lower().split()).most_common(5))
