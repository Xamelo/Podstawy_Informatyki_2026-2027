def zad1():
    #dane użytkownika
    userName = input('Podaj imię: ')
    userSurname = input('Podaj nazwisko: ')
    userCompanyName = input('Podaj nazwę firmy: ')
    userCompanyPosition = input('Podaj stanowisko w firmie: ')
    userPhoneNumer = input("Podaj numer telefonu: ")
    userMail = input('Podaj email: ')

    #długości danych użytkownika do wyświetlenia
    nameWidth = len("Imie: " + userName)
    surnameWidth = len("Nazwisko: " + userSurname)
    companyNameWidth = len("Nazwa firmy: " + userCompanyName)
    companyPositionWidth = len("Stanowisko w firmie: " + userCompanyPosition)
    phoneNumerWidth = len("Numer telefonu: " + userPhoneNumer)
    mailWidth = len("Email: " + userMail)

    #ustalanie najdłuższej danej by ustalić główną szerokość wizytówki
    mainWidth = nameWidth

    if surnameWidth > mainWidth:
        mainWidth = surnameWidth
    if companyNameWidth > mainWidth:
        mainWidth = companyNameWidth
    if companyPositionWidth > mainWidth:
        mainWidth = companyPositionWidth
    if phoneNumerWidth > mainWidth:
        mainWidth = phoneNumerWidth
    if mailWidth > mainWidth:
        mainWidth = mailWidth

    #wyświetlanie wizytówki
    print("=" * (mainWidth + 4))  #pomnożenie znaku przez n liczbę wypisze go n krotnie

    print("| Imię: " + userName + " " * (mainWidth - nameWidth) + " |")
    print("| Nazwisko: " + userSurname + " " * (mainWidth - surnameWidth) + " |")
    print("| Nazwa firmy: " + userCompanyName + " " * (mainWidth - companyNameWidth) + " |")
    print("| Stanowisko w firmie: " + userCompanyPosition + " " * (mainWidth - companyPositionWidth) + " |")
    print("| Numer telefonu: " + userPhoneNumer + " " * (mainWidth - phoneNumerWidth) + " |")
    print("| Email: " + userMail + " " * (mainWidth - mailWidth) + " |")

    print("=" * (mainWidth + 4))

def zad2():
    userCreatedPassword = input('Utwórz hasło: ')
    userPassword = input('Podaj hasło: ')

    if  userCreatedPassword == userPassword: #czy hasła są takie same
        if int(input('podaj wynik działania: 2 + 2: ')) == 4: #dwustopniowa weryfikacja
            print('Dostęp przyznany')
        else:
            print('Zła odpowiedź')
    else:
        print('Brak dostępu')

def zad3():
    #aktualna data
    currentYear = 2026
    currentMonth = 11
    currentDay = 8

    #data urodzin podana od użytkownika
    userBirthYear = int(input('Podaj rok urodzenia: '))
    userBirthMonth = int(input('Podaj miesiąc urodzin: '))
    userBirthDay = int(input('Podaj dzień urodzin: '))

    if currentYear - userBirthYear > 18:
        print('Dostęp przyznany')
    elif currentYear - userBirthYear < 18:
        print('Brak dostępu')
    else:  #currentYear - userBirthYear == 18 - jeśli ma dokładnie 18 lat trzeba sprawdzić miesiąc
        if currentMonth - userBirthMonth > 0:
            print('Dostep przyznany')
        elif currentMonth - userBirthMonth < 0:
            print('Brak dostępu')
        else: #jeśli urodził się w dokładnie aktualnym miesiącu trzeba sprawdzić dzień
            if currentDay - userBirthDay >= 0:
                print('Dostep przyznany')
            else:
                print('Brak dostępu')

#zad1()
#zad2()
zad3()
