import datetime

print("Вкажіть вартість замовлення:")
a=float(input())
b=((a + a*0.14) + (a * 0.18))

print("Оплата становить:" , "%.2f" % b)


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
