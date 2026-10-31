def yetkazish_haqi(narx, haq=5000):
    return narx + haq


qismlar = input("Narx va yetkazish haqini bo‘sh joy bilan kiriting (haq ixtiyoriy): ").split()
narx = int(qismlar[0])

if len(qismlar) > 1:
    haq = int(qismlar[1])
    print(yetkazish_haqi(narx, haq))
else:
    print(yetkazish_haqi(narx))
