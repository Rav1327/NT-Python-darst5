def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


def ijobiy_yigindi(*sonlar):
    yigindi = 0
    for son in sonlar:
        if son > 0:
            yigindi = yigindi + son
    return yigindi


n = int(qator_ol("Sonlar sonini kiriting: "))
sonlar = []

if n > 0:
    sonlar = list(map(int, qator_ol("Sonlarni bo‘sh joy bilan kiriting: ").split()))

print(ijobiy_yigindi(*sonlar))
