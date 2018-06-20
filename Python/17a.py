import datetime

print("Вкажіть суму яку ви поклали на рахунок:")
a=int(input())

a1 = a + a * 0.14
a2 = a1 + a1 * 0.14
a3 = a2 + a2 * 0.14

print("Перший рік:" , "%.2f" % a1 , "Другий рік:" , "%.2f" % a2 , "Третій рік:" , "%.2f" % a3)


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

