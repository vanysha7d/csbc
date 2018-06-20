import datetime

print("Вкажіть рік:")
year=int(input())

if (year % 400 == 0):
    print("Високосний:")
elif (year % 100 == 0):
    print("Невисокосний")
elif (year % 4 == 0):
    print("Високосний")
else:
    print("Невисокосний")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
