import datetime

print("Вкажіть висоту:")
d=int(input())

Vf=((2 * 9.8 * d) ** 0.5)

print("Vf:" , Vf)



def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
