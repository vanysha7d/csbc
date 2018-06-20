import datetime


factor = 2
n = int(input(''))
if n < 2:
    print('Error')
while factor <= n:
    if n % factor == 0:
         print(n // factor)
    else:
        factor += 1


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

