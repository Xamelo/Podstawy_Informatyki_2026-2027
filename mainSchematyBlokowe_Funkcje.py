def zad1_1():
    year = int(input('Podaj rok: '))
    #sprawdzenie czy rok jest przestępny
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Rok jest przestępny')
    else:
        print('Rok nie jest przestępny')


def zad1_2():
    dayNumber = int(input('Podaj numer dnia: '))
    #zmiana numeru dnia tygodnia na jego nazwę
    match dayNumber:
        case 1:
            print('Poniedziałek')
        case 2:
            print('Wtorek')
        case 3:
            print('Środa')
        case 4:
            print('Czwartek')
        case 5:
            print('Piątek')
        case 6:
            print('Sobota')
        case 7:
            print('Niedziela')
        case _:
            print('Zły numer dnia tygodnia')


def zad1_3():
    list = []
    number = 1
    #wpisywanie wyłącznie liczb większych od 0
    while number != 0:
        number = int(input('Podaj liczbę: '))
        if number > 0:
            list.append(number)
        else:
            continue

    #sprawdzenie czy lista jest pusta
    if len(list) == 0:
        print('Brak liczb dodatnich')
    else:
        print(f'długość listy: {len(list)}')

        sum = 0
        evenNumbers = 0

        #dodawanie liczb i liczenie wszystkich parzystych
        for number in list:
            sum += number
            if number % 2 == 0:
                evenNumbers += 1

        #wyświetlanie wszystkich informacji o liczbach
        print(f'suma podanych liczb: {sum}')
        print(f'średnia podanych liczb: {sum / len(list)}')
        print(f'ilość liczb parzystych: {evenNumbers}')
        list.sort()
        list.reverse()
        print(f'posortowana lista malejąco: {list}')
        print(f'największa liczba z listy: {list[0]}')
        print(f'najmniejsza liczba z listy: {list[-1]}')
        print(f'różnica największej i najmniejszej liczby z listy: {list[0] - list[-1]}')


def zad1_4():
    text = input('Podaj napis: ')
    print(f'długość napisu: {len(text)}')
    print(f'pierwsza litera: {text[0]}')
    print(f'ostatnia litera: {text[-1]}')
    print(f'pierwsze 3 znaki: {text[0:3]}')

    #wypisywanie wszystkich indeksów liter z wyrazu
    index = 0
    for letter in text:
        print(f'{index}: {letter}')
        index += 1

    #odwrócenie wyrazu
    reversedText = ''
    for i in range(len(text) - 1, -1, -1):
        reversedText += text[i]

    #sprawdzenie czy wyraz jest palindromem
    if reversedText == text:
        print('wyraz jest palindromem')

    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó')

    #liczenie samogłosek
    sumOfVowels = 0
    for letter in text:
        for vowel in vowels:
            if letter == vowel:
                sumOfVowels += 1
    print(f'liczba samogłosek: {sumOfVowels}')


def zad1_5():
    monday = {"Anna", "Piotr", "Marta", "Jan", "Ewa"}
    wednesday = {"Piotr", "Kasia", "Jan", "Tomek"}

    #wszustkie osoby z poniedziałku i środy
    print('Wszyscy: ', monday | wednesday)
    #osoby tylko będące w poniedziałek
    print('Poniedziałek: ', monday - wednesday)
    #osoby będące w obydwa dni
    print('Obydwa dni: ', monday & wednesday)
    #osoby będące tylko w jednym dniu
    print('Tylko jeden dzień: ', monday ^ wednesday)

    #dodanie do poniedziałku jednej osoby i usunięcie jednej osoby
    monday.add("Tomek")
    monday.discard("Ewa")

    #wyświetlenie czy zbiory są rozłączne
    print('Czy zbiory są rozłączne ', monday.issubset(wednesday))

    grades = {"Anna": 5, "Piotr": 3, "Marta": 4}

    grades["Kasia"] = 5

    grades["Piotr"] = 4

    #wypisanie imienia i oceny tej osoby
    for name, grade in grades.items():
        print(f'{name}: {grade}')

    #obliczanie średniej
    avg = sum(grades.values()) / len(grades)
    print(f'średnia: {avg}')

    #szukanie studenta i wyświetlanie jego oceny jeśli jest
    searchingStudent = input('Podaj imię studenta: ')

    if searchingStudent in grades:
        print(f'ocena: {grades[searchingStudent]}')
    else:
        print('Nie ma takiego studenta')


#zad1_1()
#zad1_2()
#zad1_3()
#zad1_4()
#zad1_5()

def zad2_1():
    chickensAmount = int(input('Podaj liczbę kur: '))
    cowsAmount = int(input('Podaj liczbę krów: '))
    pigsAmount = int(input('Podaj liczbę świń: '))

    #funckcja typu lamba, która zwraca sumę liczby zwierząt danego gatunku pomnożoną przez liczbę ich nóg
    animals = lambda chicks, cows, pigs : chicks * 2 + cows * 4 + pigs * 4

    print(f'Liczba nóg wszystkich zwierząt: {animals(chickensAmount, cowsAmount, pigsAmount)}')

def zad2_2():
    celsiusDegrees = int(input('Podaj ilość stopni celcjusza: '))

    #funkcja typu lambda, która zwraca ilość stopni fahrenheita z celsjusza
    celsiusToFahrenheit = lambda cd : (celsiusDegrees * 1.8) + 32

    print(f'Ilość stopni Fahrenheita: {celsiusToFahrenheit(celsiusDegrees)}')

def zad2_3():
    import math

    #funkcja do wyświetlania opcji
    def showMenu():
        print('1. Dodawanie')
        print('2. Odejmowanie')
        print('3. Mnożenie')
        print('4. Dzielenie')
        print('5. Reszta z dzielenia')
        print('6. Potęgowanie')
        print('7. Pierwiastkowanie')
        print('8. Wyjście')

    #funckja sumy
    add = lambda a, b: a + b
    #funkcja odejmowania
    sub = lambda a, b: a - b
    #funkcja mnożenia
    multi = lambda a, b: a * b
    #funkcja dzielenia
    def devide(a, b):
        if b == 0:
            return print('Nie można dzielić przez 0')
        else:
            return a / b
    #funkcja reszty z dzielenia
    mod = lambda a, b: a % b
    #funkcja potęgowania
    def pwr(a, b):
        result = 0
        for _ in range(b - 1):
            result += a * a
        return result
    #funkcja pierwiastkowania
    def sqroot(a, b):
        if a + b < 0:
            return 'Liczba pod pierwiastkiej nie może być ujemna'
        else:
            return math.sqrt(a + b)

    #stopuje program po wyświetleniu wyniku i kontuunuje po wpisaniu czegokolwiek
    continueProgram = lambda : input('Wpisz cokolwiek by kontynuówać: ')

    #pobieranie liczb od użytkownika
    def getUserNumbers():
        num1 = int(input('Podaj pierwszą liczbę: '))
        num2 = int(input('Podaj drugą liczbę: '))
        return [num1, num2]

    #obsługa wybranej opcji z menu
    def doChoice(option):
        match (option):
            case '1':
                nums = getUserNumbers()
                print(f'Wynik dodawania {nums[0]} oraz {nums[1]} wynosi: {add(nums[0], nums[1])}')
                continueProgram()
            case '2':
                nums = getUserNumbers()
                print(f'Wynik odejmowania {nums[0]} oraz {nums[1]} wynosi: {sub(nums[0], nums[1])}')
                continueProgram()
            case '3':
                nums = getUserNumbers()
                print(f'Wynik mnożenia {nums[0]} oraz {nums[1]} wynosi: {multi(nums[0], nums[1])}')
                continueProgram()
            case '4':
                nums = getUserNumbers()
                print(f'Wynik dzielenia {nums[0]} oraz {nums[1]} wynosi: {devide(nums[0], nums[1])}')
                continueProgram()
            case '5':
                nums = getUserNumbers()
                print(f'Wynik reszty z dzielenia {nums[0]} oraz {nums[1]} wynosi: {mod(nums[0], nums[1])}')
                continueProgram()
            case '6':
                nums = getUserNumbers()
                print(f'Wynik potęgowania {nums[0]} oraz {nums[1]} wynosi: {pwr(nums[0], nums[1])}')
                continueProgram()
            case '7':
                nums = getUserNumbers()
                print(f'Wynik pierwiastkowania sumy {nums[0]} i {nums[1]} wynosi: {sqroot(nums[0], nums[1])}')
                continueProgram()
            case '8':
                return True
            case _:
                againOption = ''
                while againOption != '0':
                    againOption = input('Nie ma takiej opjci, wpisz 0 by znów wybrać: ')

    #działanie kalkulatora w pętli
    while (True):
        showMenu()
        option = input('Podaj opcję: ')
        #jeśli użytkownik wpisze 8 - pętla się zakończy
        if doChoice(option):
            break


def zad2_4():
    import random

    #tworzenie zmiennych globalnych jako wynik graczy
    global userScore, aiScore
    userScore = 0
    aiScore = 0

    #funkcja wyświetlająca wynik
    def showScore():
        print(f'Wynik gracza: {userScore}')
        print(f'Wynik komputera: {aiScore}')

    #funkcja wyświetlająca wybory dla użytkownika
    def showOptions():
        print('1. Kamień')
        print('2. Papier')
        print('3. Nożyce')
        print('0. Zakończ grę')

    #funkcja losująca wybór komputera
    randomizeAiChoice = lambda : str(random.randint(1, 3))

    #funkcja pobierająca od użytkownika wybór
    getUserChoice = lambda : input('Wyybierz opcję: ')

    #funkcja porównywująca wybory
    def compareChoices():
        global userScore, aiScore
        userChoice = getUserChoice()
        randomAiChoice = randomizeAiChoice()

        #remis gdy komputer wybrał to samo
        if randomAiChoice == userChoice:
            print('remis - komputer wybrał to samo')
            aiScore += 1
            userScore += 1
        else:
            #porównywanie wyboru gdy komputer wybrał coś innego
            match userChoice:
                #użytkownik wybrał kamień
                case '1':
                    if randomAiChoice == '2':
                        print('przegrałeś, komputer wybrał papier')
                        aiScore += 1
                    else:
                        print('wygrałeś - komputer wybrał nożyce')
                        userScore += 1
                #użytkownik wybrał papier
                case '2':
                    if randomAiChoice == '1':
                        print('wygrałeś - komputer wybrał kamień')
                        userScore += 1
                    else:
                        print('przegrałeś - komputer wybrał nożyce')
                        aiScore += 1
                #użytkownik wybrał nożyce
                case '3':
                    if randomAiChoice == '1':
                        print('przegrałeś - komputer wybrał kamień')
                        aiScore += 1
                    else:
                        print('wygrałeś - komputer wybrał papier')
                        userScore += 1
                #gdy użytkownik wpisze 0 - gra się zakończy i wyświetli wynik
                case '0':
                    print('Gra zakończona, ostateczny wynik: ')
                    showScore()
                    return True
                # gdy użytkownik wpisze coś z poza zakresu
                case _ :
                    print('wybierz jeszcze raz: ')
                    compareChoices()

    #działanie gry w pętli
    while (True):
        showOptions()
        #jeżeli użytkownik wpisał 0 to funkcja compareChoices() zwróci wartość True i pętla się zakończy
        if compareChoices():
            break
        showScore()
#zad2_1()
#zad2_2()
#zad2_3()
zad2_4()
