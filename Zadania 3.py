print("ZADANIE 1.")
dane = str([x*2 for x in range(0,31)])
plik = open("Zad1.txt","w+")
plik.writelines(dane)
plik.close()

print("\nZADANIE 2.")
plik = open("Zad1.txt","r")
odczyt = plik.readline()
print(odczyt)
plik.close()

print("\nZADANIE 3.")
tekst = "Litwo! Ojczyzno moja! Ty DDjesteś jak zdrowie. Nazywał się niedawno w wielkiej peruce, którą do ojca Podkomorzego"
with open("Zad3.txt","w+") as plik:
    plik.writelines(tekst)
with open("Zad3.txt","r+") as plik:
    for linia in plik:
        print(linia,end="")

print("\nZADANIE 4.")
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednosta_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednosta_miary
        self.cena_jed=cena_jed

    def wyswietl_produkt(self):
        print("Produkt:", self.nazwa_produktu)
        print("Ilość:", self.ilosc,self.jednostka_miary)
        print("Cena:",self.cena_jed)

    def ile_produktu(self):
        return str(self.ilosc) + "" + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

ziemniaki = NaZakupy("ziemniaki", 3, "kg", 2)
ziemniaki.wyswietl_produkt()
print("Ilość:", ziemniaki.ile_produktu())
print("Koszt:", ziemniaki.ile_kosztuje(), "zł")

print("\nZADANIE 5.")
class ciagi_arytmetyczne:
    def __init__(self):
        self.elementy=[]
    def wyswietl_dane(self):
        print(self.elementy)
    def pobierz_elementy(self):
        ilosc=int(input("Ilosc elementow:"))
        for i in range(ilosc):
            self.elementy.append(int(input(f"Podaj element {i+1}:")))
    def pobierz_parametry(self):
        a=int(input("Podaj pierwszy element ciągu:"))
        r=int(input("Podaj roznice ciagu:"))
        n=int(input("Podaj ilosc elementow ciagu do wygenerowania:"))
        self.elementy = [a+ i*r for i in range(n)]
    def policz_sume(self):
        suma = sum(self.elementy)
        print(f"Suma elementow:{suma}")
    def policz_elementy(self,a,r,n):
        elementy = [a + i*r for i in range(n)]
        print(f"losc elementow:{elementy}")

ciag = ciagi_arytmetyczne()
ciag.pobierz_elementy()
ciag.wyswietl_dane()
ciag.pobierz_parametry()
ciag.wyswietl_dane()
ciag.policz_sume()
ciag.policz_elementy(2, 3, 5)



print("\nZADANIE 6.")
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
    def pokaz_gdzie_jestes(self):
        print("Współrzędne:",self.x,",",self.y)

robaczek = Robaczek(0, 0, 1)
robaczek.idz_w_prawo(12)
robaczek.idz_w_gore(7)
robaczek.idz_w_lewo(4)
robaczek.idz_w_dol(11)
robaczek.pokaz_gdzie_jestes()


