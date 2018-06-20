import datetime

print("Напишіть 1 якщо використовуєте дюйми та фунти ,або 2 якщо метри та кілометри:")
a=input()

if a=="1":
    print("Вкажіть масу:")
    b=int(input())
    print("Вкажіть зріст:")
    c=int(input())
    IMT=(703 * (b / (c ** 2)))
    print("IМТ:")
    print(IMT)
elif a=="2":
    print("Вкажіть масу:")
    b=int(input())
    print("Вкажіть зріст:")
    c=int(input())
    IMT=(b / (c ** 2))
    print("IМТ:")
    print(IMT)
else:
    print("Помилка")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
