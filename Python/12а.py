import datetime

print("Вкажіть кількість днів:")
day=int(input())
print("Вкажіть кількість годин:")
hour=int(input())
print("Вкажіть кількість хвилин:")
minute=int(input())
print("Вкажіть кількість секунд:")
second=int(input())

print(((day * 86400) + (hour * 3600) + (minute * 60) + second) ,"секунд")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
