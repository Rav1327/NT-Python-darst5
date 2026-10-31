baholar = list(map(int, input("Baholarni bo‘sh joy bilan kiriting: ").split()))

yuqori_baholar = list(filter(lambda baho: baho > 70, baholar))
print(yuqori_baholar)
