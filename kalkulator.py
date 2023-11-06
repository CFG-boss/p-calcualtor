import math

# Prosty kalkulator w Pythonie z funkcją pierwiastka

# Funkcja dodawania
def dodawanie(a, b):
    return a + b

# Funkcja odejmowania
def odejmowanie(a, b):
    return a - b

# Funkcja mnożenia
def mnozenie(a, b):
    return a * b

# Funkcja dzielenia
def dzielenie(a, b):
    if b == 0:
        return "Błąd: Nie można dzielić przez zero!"
    return a / b

# Funkcja procentu
def procent(a, b):
    return (a * b) / 100

# Funkcja pierwiastka kwadratowego
def pierwiastek(a):
    if a < 0:
        return "Błąd: Nie można obliczyć pierwiastka z liczby ujemnej"
    return math.sqrt(a)

# Główna pętla programu
while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Procent")
    print("6. Pierwiastek kwadratowy")
    print("7. Zakończ")

    wybor = input("Podaj numer operacji: ")

    if wybor == '7':
        print("Kalkulator został zakończony.")
        break

    if wybor not in ('1', '2', '3', '4', '5', '6'):
        print("Nieprawidłowy wybór. Wybierz ponownie.")
        continue

    liczba1 = float(input("Podaj pierwszą liczbę: "))

    if wybor != '5' and wybor != '6':
        liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print("Wynik: ", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print("Wynik: ", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print("Wynik: ", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print("Wynik: ", dzielenie(liczba1, liczba2))
    elif wybor == '5':
        procent_input = float(input("Podaj procent: "))
        print("Wynik: ", procent(liczba1, procent_input))
    elif wybor == '6':
        print("Wynik: ", pierwiastek(liczba1))