import datetime

print("Чи говорить зараз папуга?")
a=input()

print("Котра година?")
b=float(input())

if a=="так":
    if 22.00<=b<=24.00 or 0.00<=b<=8.00:
        print("Накривайте рядниною")
    elif 8.00<b<22.00:
        print("Все нормально")
    else:
        print("Помилка")
elif a=="ні":
    print("Все нормально")
else:
    print("Помилка")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

                   
