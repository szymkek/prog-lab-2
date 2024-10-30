#zadanie 1

x = float(input("podaj liczbę zdobytych punktów:\n "))

if x >= 80:
    print("egzamin zaliczony w terminie 0\n")
elif x >= 50 and x <= 80:
    print("egzamin zaliczony ale można go poprawić\n")
else:
    print("egzamin niezaliczony\n")

#zadanie 2

x = float(input("podaj liczbę 1: "))
y = float(input("podaj liczbę 2: "))
z = float(input("podaj liczbę 3: "))
print("\n")

if x > y:
    x,y=y,x
if x > z:
    x,z=z,x
if y > z:
    y,z-z,y
print(f"liczby w kolejności losowej {x},{y},{z}\n")

#zadanie 6

litera = input("podaj literę: ")

if litera.isalpha() and len(litera) == 1:
    if litera.isupper():
        print("litera jest duża\n")
    if litera.islower():
        print("litera jest mała\n")

else:
    print("podany znak nie jest pojedynczą literą\n")


#zadanie 7

hasło = 'pk47!jy0893'

if len(hasło) >= 11:
    print("hasło jest poprawne\n")
else:
    print("hasło jest nie poprawne\n")

#zadanie 8

text = 'Studiuje-Informatykę'

pierwsze_trzy_znaki = text[:3]
print("pierwsze trzy znaki:\n ", {pierwsze_trzy_znaki})

ostatnie_dwa_znaki = text[-2:]
print("ostatnie dwa znaki:\n ", {ostatnie_dwa_znaki})

#zadanie 5

plik = open("notowania giełdowe.txt", "r")
if plik.readable():
    tekst = plik.read()
    print(tekst, end='\n')
    print("ALR, 113\n")

#zadanie 3

Nzawa_pliku = "Raport_maj.xlsx"

if Nzawa_pliku.endswith(".xlsx"):
    print("tak")
else:
    print("nie")









