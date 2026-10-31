def katta_son(a, b):
    if a >= b:
        return a
    else:
        return b


qismlar = input("Ikkita sonni bo‘sh joy bilan kiriting: ").split()
a = int(qismlar[0])
b = int(qismlar[1])
print(katta_son(a, b))
