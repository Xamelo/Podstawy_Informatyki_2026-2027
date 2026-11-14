def zad1():
    year = int(input('Podaj rok: '))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Rok jest przestępny')
    else:
        print('Rok nie jest przestępny')

def zad2():
    dayNumber = int(input('Podaj numer dnia: '))
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

def zad3():
    list = []
    number = 1
    while number != 0:
        number = int(input('Podaj liczbę: '))
        if number > 0:
            list.append(number)
        else:
            continue
    if len(list) == 0:
        print('Brak liczb dodatnich')
    else:
        print(f'długość listy: {len(list)}')

        sum = 0
        evenNumbers = 0
        for number in list:
            sum += number
            if number % 2 == 0:
                evenNumbers += 1

        print(f'suma podanych liczb: {sum}')
        print(f'średnia podanych liczb: {sum / len(list)}')
        print(f'ilość liczb parzystych: {evenNumbers}')
        list.sort()
        list.reverse()
        print(f'posortowana lista malejąco: {list}')
        print(f'największa liczba z listy: {list[0]}')
        print(f'najmniejsza liczba z listy: {list[-1]}')
        print(f'różnica największej i najmniejszej liczby z listy: {list[0] - list[-1]}')

def zad4():
    text = input('Podaj napis: ')
    print(f'długość napisu: {len(text)}')
    print(f'pierwsza litera: {text[0]}')
    print(f'ostatnia litera: {text[-1]}')
    print(f'pierwsze 3 znaki: {text[0:3]}')

    index = 0
    for letter in text:
        print(f'{index}: {letter}')
        index += 1

    reversedText = ''
    for i in range(len(text) - 1, -1, -1):
        reversedText += text[i]

    if reversedText == text:
        print('wyraz jest palindromem')

    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó')

    sumOfVowels = 0
    for letter in text:
        for vowel in vowels:
            if letter == vowel:
                sumOfVowels += 1
    print(f'liczba samogłosek: {sumOfVowels}')

def zad5():
    monday = {"Anna", "Piotr", "Marta", "Jan", "Ewa"}
    wednesday = {"Piotr", "Kasia", "Jan", "Tomek"}

    print('Wszyscy: ', monday | wednesday)
    print('Poniedziałek: ', monday - wednesday)
    print('Oba dni: ', monday & wednesday)
    print('Tylko jeden dzień: ', monday ^ wednesday)

    monday.add("Tomek")
    monday.discard("Ewa")

    print('Czy zbiory są rozłączne ', monday.issubset(wednesday))

    grades = {"Anna": 5, "Piotr": 3, "Marta": 4}

    grades["Kasia"] = 5

    grades["Piotr"] = 4

    for name, grade in grades.items():
        print(f'{name}: {grade}')

    avg = sum(grades.values()) / len(grades)
    print(f'średnia: {avg}')

    searchingStudent = input('Podaj imię studenta: ')

    if searchingStudent in grades:
        print(f'ocena: {grades[searchingStudent]}')
    else:
        print('Nie ma takiego studenta')


#zad1()
#zad2()
#zad3()
#zad4()
zad5()