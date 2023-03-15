import math
def pierwiastek(a,stopien):
    pierw=pow(a,1/stopien)
    return pierw

print('ZADANIE 1.')
wynik1=math.exp(10)
print(wynik1)
wynik2=pierwiastek(math.log(5+pow(math.sin(8),2),math.e),6)
print(wynik2)
wynik3=math.floor(3.55)
print(wynik3)
wynik4=math.ceil(4.80)
print(wynik4)

print('ZADANIE 2.')
imie = 'BARTLOMIEJ'
nazwisko = 'SLESINSKI'
imie.lower()
nazwisko.lower()
imie.capitalize()
nazwisko.capitalize()
print(imie)
print(nazwisko)

print('ZADANIE 3.')
tekst = 'Running away is easy Its the leaving thats hard Time Running away is easy Time Time Its the leaving thats hard Time Time Time'
txt = tekst.count("Time")
print(txt)

print('ZADANIE 4.')
z4 = 'hhasdgoiagrj'
print(z4[1])
print(z4[-1])

print('ZADANIE 6.')
name = 'Bartek'
age = 20
height = 1.70
print('imie to {} i wiek to {} a wzrost to {} m.'.format(name,age,height))

print('ZADANIE 5.')
text = 'imie to {} i wiek to {} a wzrost to {} m.'.format(name,age,height)
x = text.split(' ')
print(x)

print('ZADANIE 7.')
sporty = ['box','siatkowka','koszykowka','pilka nozna']
sporty.reverse()
sporty.append('plywanie')
print(sporty)

print('ZADANIE 8.')
skroty = {
    'FAQ':'najczęściej zadawane pytania',
    'DIY': 'zrób to sam',
    'FYI': 'dla twojej informacji',
    'IMO': 'moim zdaniem'
}
print(skroty)

print('ZADANIE 9.')
gry = {
    'FPS' : ['Call of Duty','Battlefield'],
    'horror' : ['Alien','Amnesia'],
    'detektywistyczne': ['Pigment','Return of Obradin']
}
print(gry)
print('liczba elementow w slowniku : {}.'.format(len(gry)))

print('ZADANIE 10.')
zdanie = input('Napisz zdanie:')
print('litera a wystepuje {} razy'.format(zdanie.count('a')))

print('ZADANIE 11.')
a = int(input('podaj a :'))
b = int(input('podaj b :'))
c = int(input('podaj c :'))
print('najwieksza liczba : {}.'.format(max(a,b,c)))

print('ZADANIE 12.')
lista = [12,4.6,24,3.5,8,9,2.1,0.5]
for i in lista:
    x = pow(i,2)
    print(x)

print('ZADANIE 13.')
parzyste = []
i = 0
while i < 10:
    l = int(input('podaj liczbe {}: '.format(i+1)))
    if l%2==0:
        parzyste.append(l)
    i+=1
print(parzyste)