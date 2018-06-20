import datetime

print("Введіть довжину(см):")
a=int(input())
print("Введіть ширину(см):")
b=int(input())
S=(a * b)
Ga=(S / 10000)
A=(Ga / 0.01)

print(Ga , "Гектарів та" , A , "Арів")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
