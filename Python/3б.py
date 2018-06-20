import datetime


sp1 = []
sp = []

while 1:
    a = float(input('Введіть значення в Цельсіях (введіть 1 щоб перестати вводити значення): '))
    sp1.append(a)
    b = a % 10
    if b == 0 and a >= 0 and a <= 100:
        c = a * 9/5 + 32
        sp.append(c)
    elif a == 1:
        break
    else:
        print('Помилка')
for i in range(len(sp)):
    print('{0} °C       ==>       {1} ºF'.format(sp1[i], sp[i]))




def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)
