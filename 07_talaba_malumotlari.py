def qator_ol(sorov):
    qator = input(sorov)
    while qator.strip() == "":
        qator = input()
    return qator


def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(kalit.capitalize() + ": " + str(qiymat))


ism = qator_ol("Talaba ismini kiriting: ")
kurs = qator_ol("Kursni kiriting: ")
shahar = qator_ol("Shaharni kiriting: ")
talaba_info(ism=ism, kurs=kurs, shahar=shahar)
