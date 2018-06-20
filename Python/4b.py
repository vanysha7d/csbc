import datetime

print("Вкажіть кількість дзвінків:")
a=int(input())

print("Вкажіть кількість смс:")
b=int(input())

c=15

if a > 200:
    c += (a - 200) * 0.17

if b > 50:
    c += (b - 50) * 0.15

d=(c + c * 0.05 + 0.44)

print("Без внесків та податків:" , "%.2f" % c , "$")
print("З внесками та податками:" , "%.2f" % d , "$")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

