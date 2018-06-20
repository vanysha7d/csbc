import datetime


a = 1
b = []
while True:
    a = int(input('Введіть число: '))
    if a != 0:
        b.append(a)
    else:
        break
if b[0] == 0:
    print('Помилка!')
else:
    print('Середнє значення: ' + str(sum(b) / len(b)))


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
