import datetime

print("Вкажіть дані:")
a=input()

if a=="вихідний":
    print("не включати будильник")
elif a=="відпустка":
    print("не включати будильник")
elif a=="будні":
    print("включити будильник")
else:
    print("Помилка")



def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
