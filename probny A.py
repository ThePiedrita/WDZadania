import math
print("ZADANIE 1.")
try:
    a = int(input("Podaj liczbe a: "))
    b = int(input("Podaj liczbe b: "))
    wynik = str(pow(a,2)+a*b+pow(b,2))

    with open("zadanie1.txt","w+") as plik:
        plik.writelines("Wynik: "+wynik)
    print(wynik)
except:
    print("Wprowadz calkowite wartosci")

print("\nZADANIE 2.")
lista1=[2,4,3,5,6,4]
lista2=[5,4,3,6,3,1,9]
lista_sum=[]
def sum():
    while len(lista1)!= len(lista2):
        if len(lista1)>len(lista2):
            lista2.append(0)
        else:
            lista1.append(0)
    for i in range(0,max(len(lista1),len(lista2))) :
        lista_sum.append(int(lista1[i])+int(lista2[i]))

    print(lista_sum)
sum()

print("\nZADANIE 3.")
with open("tekst.txt","r",encoding="utf-8") as plik:
    znaki=plik.read()[100:135]

duze_znaki=[znak for znak in znaki if znaki.isupper()]

if duze_znaki:
    print(f"Duze znaki: {', '.join(duze_znaki)}")
    print(f"Ilosc duzych liter: {len(duze_znaki)}")
else:
    print("brak duzych znakow")

print("\nZADANIE 4.")
a=5
list=[4,6,7,5,1,2,3,5,7]
list_a=[i for i in list if i>a]
print(list_a)

print("\nZADANIE 5.")
wynik=math.pow(math.exp(3)+math.pow(math.cos(39),2),1/5)+math.pow(5/7,3)+math.pi
wynik=round(wynik,2)
print(wynik)





