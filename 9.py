#Irjon egy függvényt, ami listában kap meg számokat b1 számrendszerbe ábrázolva és
#b2 számrendszerbe konvertálja azokat. A függvény paraméterként kapja a b1, b2
#számokat is
try:
    szam=[1211,2000,1021]
    mibol=int(input("Melyik szamrendszerből szeretné átváltani a számot?"))
    szamrendszer=int(input("Melyik szamrendszerbe szeretné átváltani a számot?"))
    maradek=0
    def valt(szam, szamrendszer):
        global osszeg
        szamok = []
        ls=[]
        while osszeg > 0:
            maradek=osszeg%szamrendszer  #sima 10-es számrendszerből való átváltás
            osszeg=osszeg//szamrendszer  #
            if maradek < 10:
                szamok.append(maradek)
            else:
                szamok.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[maradek])
        print("A szám {0} számrendszerbeli alakja:".format(szamrendszer),"".join(map(str,szamok[::-1])))
    def tizesbe(szam,mibol):
        global osszeg
        for j in szam:
            osszeg=0
            j=str(j)
            hossz=len(j)
            for i in range(hossz):
                osszeg=(mibol**(hossz-1-i))*"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(j[i])+osszeg #hatványozással vált át tizebe
            print("A szám 10-es számrendszerbeli alakjai:",osszeg)
            valt(osszeg,szamrendszer)
    tizesbe(szam,mibol)
except ValueError:
    print("Hibás az input, kérlek számot adj meg számrendszernek")

#Nekem úgy volt a legegyszerübb konvertálni, hogy először 10-es számrendszerbe váltom és onnan a kívánt számrendszerbe
#A program nem veszi észre ha pl kap egy olyan számot hogy "220" és a felhasználó azt mondja, hogy ez kettes számrendszerben
#van megcsinálja, de az eredmény hibás lesz.
#Két fv-t írtam a tizesbe(): valamilyen számrendszerből 10-e számrendszerbe váltja a kívánt számokat
#A vált fv pedig 10-esből vált a várt számrendszerbe.
#a map() a listámat alakítja str-é és a szamokat fűzi össze joinnal