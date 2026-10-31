def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


n = int(qator_ol("Mahsulotlar sonini kiriting: "))
narxlar = []

if n > 0:
    narxlar = list(map(int, qator_ol("Narxlarni bo‘sh joy bilan kiriting: ").split()))

qimmatlar = list(filter(lambda narx: narx >= 15000, narxlar))
chegirmali = list(map(lambda narx: narx - 3000, qimmatlar))
print(chegirmali)
