import datetime

print("Вкажіть зріст(см):")
a=int(input())
b=(a // 2.54)
F=(b // 12)
D=(b % 12)

print(F ,"Фунтів та " , D ,"Дюймів")



def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
