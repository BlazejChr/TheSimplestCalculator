#Zmienne
liczba_pierwsza = input("Podaj pierwszą liczbę:" )
liczba_druga = input("Podaj drugą liczbę: ")

#Operacje
dodawanie = int(liczba_pierwsza) + int(liczba_druga)
odejmowanie = int(liczba_pierwsza) - int(liczba_druga)
mnożenie = int(liczba_pierwsza) * int(liczba_druga)
dzielenie = int(liczba_pierwsza) / int(liczba_druga)
potęga = int(liczba_pierwsza) ** int(liczba_druga)

#Wybór
Wybor = input("Jaką operację chcesz wykonać? (Dodawanie; Odejmowanie; Mnożenie; Dzielenie; Potęgowanie) " )

#Działania do wyboru
if Wybor == 'Dodawanie':
        print("Wynik dodawania: ", dodawanie)
elif Wybor == 'Odejmowanie':
        print("Wynik odejmowania: ", odejmowanie)
elif Wybor == 'Mnożenie':
        print("Wynik mnożenia: ", mnożenie)
elif Wybor == 'Dzielenie':
        print("Wynik dzielenia: ", dzielenie)
elif Wybor == 'Potęga':
        print("Wynik potęgi: ", potęga)

#Wyprintowanie - już nie potrzebne 
#print("Wynik działania: ", )