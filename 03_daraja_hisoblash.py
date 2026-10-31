def daraja(son, n=2):
    return son ** n


qismlar = input("Son va darajani bo‘sh joy bilan kiriting (daraja ixtiyoriy): ").split()
son = int(qismlar[0])

if len(qismlar) > 1:
    n = int(qismlar[1])
    print(daraja(son, n))
else:
    print(daraja(son))
