import random
import math

print("ZADANIE 1.")
a = [1 - x for x in range(10)]
b = [x ** 7 for x in range(7)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)

print("\nZADANIE 2.")
lista1 = []
for i in range(10):
    lista1.append(random.randint(1, 20))
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista1)
print(lista2)

print("\nZADANIE 3.")
produkty = {
    "mleko":"litry",
    "chleb":"sztuki",
    "ziemniaki":"kg",
    "chipsy":"sztuki",
    "cebula":"kg",
    "woda":"litry"
}
sztuki = [produkt for produkt, jednostka in produkty.items() if jednostka == 'sztuki']
print(produkty)
print(sztuki)

print("\nZADANIE 4.")
def troj_prost(a,b,c):
    if a**2 + b**2 == c**2:
        print("Trójkąt jest prostokątny")
    elif a**2 + c**2 == b**2:
        print("Trójkąt jest prostokątny")
    elif b ** 2 + c ** 2 == a ** 2:
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")

troj_prost(6,10,8)

print("\n ZADANIE 5.")
def p_trapez(a=5,b=10,h=15):
    return((a+b)*h)/2

print(p_trapez())

print("\nZADANIE 6.")
def ciag(a1=1,b=4,ile=10):
    iloczyn = a1
    for i in range(ile):
        iloczyn *=b
    return iloczyn

print(ciag())
print(ciag(1,2,10))

print("\nZADANIE 7.")
def iloczyn_ciagu(*liczby):
    if len(liczby)==0:
        return 0
    else:
        iloczyn=1
        for i in liczby:
            iloczyn *= i
        return iloczyn
print(iloczyn_ciagu(4,2,5,7,3,7,9,3))

print("\nZADANIE 8.")
def zakupy(** produkty):
    ilosc = len(produkty.keys())
    sum_cena = sum(cena for cena in produkty.values())
    return f"Total products: {ilosc}. Total cost: {sum_cena}"

print(zakupy(piwo=5,chipsy=6,chleb=3,jajka=12,czekolada=5))

print("\nZADANIE 9.")
a = int(input("podaj liczbe:"))

try:
    wynik = math.sqrt(a)
    print(wynik)

except:
    print("liczba podana nie może być ujemna")
