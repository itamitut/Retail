import random

# генерирует случайную букву в диапазоне x - y
def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))

for i in range(9):
    r = randletter('А', 'Я')
    print(r)
