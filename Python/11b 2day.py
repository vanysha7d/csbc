import datetime

def print_menu():
    print('1. Друк телефонних номерів')
    print('2. Додати номер телефону')
    print('3. Видалити номер телефону')
    print('4. Пошук контакту')
    print('5. Вийти')
    print('')

numbers = {"Пожежна безпека": "101" , "Поліція": "102" , "Швидка допомога": "103"}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Виберіть цифру (1-5): "))
    if menu_choice == 1:
        print("Телефонні номери:")
        for x in numbers.keys():
            print("Ім'я:", x, "\tТелефон:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Додати ім'я та номер")
        name = input("Ім'я: ")
        phone = input("Номер: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Видалити ім'я та номер")
        name = input("Ім'я: ")
        number = input("Номер: ")
        print = input("Номер видален")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "не знайден")
    elif menu_choice == 4:
        print("Знайти контакт")
        name = input("Ім'я: ")
        if name in numbers:
            print("Номер телефону:", numbers[name])
        else:
            print(name, "не знайден")
    elif menu_choice != 5:
        print_menu()


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
