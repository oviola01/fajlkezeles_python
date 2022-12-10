def beolvasas(fajlnev):
    #megnyitás
    fajlom = open(fajlnev, "r", encoding = "utf-8")
    print(fajlom)
    fejlec = fajlom.readline().strip()
    print(fejlec)
    sorok = fajlom.readlines()
    print(sorok)
    fajlom.close()
    fajlfeldolg(sorok)

nevek = []
nemek = []
korok = []

def fajlfeldolg(sorok):
    #itt dolgozom fel a kapott listát
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(", ")
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1
    print(nevek)
    print(nemek)
    print(korok)

