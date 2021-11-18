import random
n = int(input('N = '))
a = []
for i in (range(n)):
    a.append(random.randint(-30, 45))
    a.sort()
    a.reverse()
print(a)




