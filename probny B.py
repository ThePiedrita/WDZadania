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
---------------------------------------------------
ZAD1
import math

expression = math.sqrt(math.log(20) + math.cos(45)+math.exp, 1/3)
rounded_result = round(expression, 2)

print(rounded_result)
#ZAD2
# Utworzenie listy z liczbami
liczby = [5, 10, 3, 8, 2, 7]

# Utworzenie nowej listy bez minimalnej liczby
nowa_lista = [x for x in liczby if x != min(liczby)]

# Wyświetlenie obu list
print("Pierwsza lista: ", liczby)
print("Nowa lista: ", nowa_lista)
#ZAD3
def filtruj_zmiennoprzecinkowe(słownik):
    zmiennoprzecinkowe = []
    for klucz, wartość in słownik.items():
        if isinstance(klucz, float) and isinstance(wartość, float):
            zmiennoprzecinkowe.append((klucz, wartość))
    return zmiennoprzecinkowe
#ZAD4
with open('tekst.txt', 'r', encoding='utf-8') as plik:
    znaki = plik.read()
    fragment = znaki[17:58]
    ilosc_c = znaki.count('c')
    plik.close()
    print("Wczytany fragment: ", fragment)
    print("Ilość wystąpień litery 'c': ", ilosc_c)
#ZAD5
try:
    a1 = int(input("Podaj pierwszy wyraz ciągu: "))
    n = int(input("Podaj numer wyrazu do obliczenia: "))
    q = int(input("Podaj iloraz ciągu: "))
except ValueError:
    print("Podano niepoprawne wartości")
else:
    an = a1 * q ** (n - 1)
    with open("wynik.txt", "w") as f:
        f.write(str(an))
    plik.close()
---------------------------------------------------
ZAD1
import math

expression = math.sqrt(math.exp(4) - math.log2(34), 1/3)
rounded_result = round(expression, 2)

print(rounded_result)
#ZAD2
# Tworzenie listy z liczbami
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tworzenie nowej listy zawierającej co trzeci element z pierwszej listy za pomocą list comprehension
every_third_number = [numbers[i] for i in range(2, len(numbers), 3)]

# Wyświetlanie obu list
print("Lista z liczbami: ", numbers)
print("Co trzeci element z listy: ", every_third_number)
#ZAD3
def check_sum_and_count(numbers):
    # Obliczanie sumy pierwszego i ostatniego elementu listy
    sum_of_first_and_last = numbers[0] + numbers[-1]

    # Liczenie elementów z listy większych od sumy pierwszego i ostatniego elementu
    count = sum(1 for num in numbers if num > sum_of_first_and_last)

    # Zwracanie wyników
    return sum_of_first_and_last, count
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_result, count_result = check_sum_and_count(numbers)
print("Suma pierwszego i ostatniego elementu: ", sum_result)
print("Liczba elementów większych niż suma: ", count_result)
#ZAD4
# Otwieranie pliku z obsługą polskich znaków
with open('tekst.txt', 'r', encoding='utf-8') as file:
    # Wczytywanie tekstu z pliku
    text = file.read()

# Wycinanie fragmentu tekstu
start_index = 49
end_index = start_index + 25
fragment = text[start_index:end_index]

# Obliczanie ilości dużych liter w fragmencie tekstu
count_upper = sum(1 for letter in fragment if letter.isupper())
plik.close()
# Wyświetlanie wyników
print("Fragment tekstu: ", fragment)
print("Ilość dużych liter: ", count_upper)
#ZAD5
import math

try:
    # Wczytanie trzech liczb od użytkownika
    a = int(input("Podaj długość pierwszej przyprostokątnej: "))
    b = int(input("Podaj długość drugiej przyprostokątnej: "))
    c = int(input("Podaj długość przeciwprostokątnej: "))

    # Sprawdzenie, czy z podanych wartości można utworzyć trójkąt prostokątny
    if a > 0 and b > 0 and c > 0 and a*a + b*b == c*c:
        # Obliczenie pola trójkąta
        pole = 0.5 * a * b

        # Zapisanie wyniku do pliku
        with open("wynik.txt", "w") as file:
            file.write(f"Pole trójkąta wynosi: {pole}")

        print("Pomyślnie obliczono pole trójkąta i zapisano wynik do pliku.")

    else:
        print("Nie można utworzyć trójkąta prostokątnego o podanych bokach.")

except ValueError:
    print("Podane wartości nie są liczbami całkowitymi.")