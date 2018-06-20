import datetime

print("Вкажіть кількість людських років:")

a=float(input())

if a<=2:
    b=(a * 5.25)
elif a>2:
    b = 10.5
    b +=4 * (a - 2)

print("Собачі роки:" , b)


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
