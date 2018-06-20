import datetime

print("Введіть пройдений шлях:")
a=int(input())

def func(a,b):
    return (((a/140) * b) + 25)
c=func(a,2)

print("Оплата:" , "%.0f" % c , "$")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
