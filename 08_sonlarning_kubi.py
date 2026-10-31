def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


n = int(qator_ol("Sonlar sonini kiriting: "))
sonlar = []

if n > 0:
    sonlar = list(map(int, qator_ol("Sonlarni bo‘sh joy bilan kiriting: ").split()))

kublar = list(map(lambda son: son ** 3, sonlar))
print(kublar)
