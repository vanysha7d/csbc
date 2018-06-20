import datetime

print("Вкажіть температуру(цельсія):")
C=int(input())
K=(C + 273.15)
F=((9 / 5) * C + 32)
print("Кельвіна:" , K)
print("Фаренгейт:" , F)



def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
