import math

print("ZADANIE 1.")
with open("tekst.txt","r",encoding="utf-8") as plik:
    znaki_a=plik.read()[71:111]
duze_a=[znaki for znaki in znaki_a if "A" in znaki_a]
if duze_a:
    print(f"Litera A sie powtarza {len(duze_a)} razy")
else:
    print("litera A nie wystepuje")

print("\nZADANIE 2.")
lista1=[4,6.5,1,2.5,"robot",7,"kon"]
przecinkowa=[x for x in lista1 if isinstance(x,float)]
print(lista1)
print(przecinkowa)

print("\nZADANIE 3.")
def dodaj_sume(lista):
    suma=sum(lista)
    lista.append(suma)
    return lista
lista=[1,2,3,4,5]
nowa_lista=dodaj_sume(lista)
print(nowa_lista)

print("\nZADANIE 4.")
wynik=math.pow(math.sin(56),2)+math.pow((math.pow(4,2)/25)+math.log(85,3),1/4)
wynik=round(wynik,2)
print(wynik)

print("\nZADANIE 5.")
try:
    n=int(input("podaj liczbe n:"))
    i=1
    suma=0
    while i<n:
        suma+=i
        i+=1
    with open("zadanie5.txt","w") as plik:
        plik.writelines(str(suma))
    print(suma)
except:
    print("liczba n musi byc calkowita i nie ujemna")
