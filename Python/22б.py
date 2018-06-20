import datetime


b = []
def iff(a):
    if a == 0:
        print('F')
    elif a == 1:
        print('D')
    elif a == 1.3:
        print('D+')
    elif a == 1.7:
        print('C-')
    elif a == 2.0:
        print('C')
    elif a == 2.3:
        print('C+')
    elif a == 2.7:
        print('B-')
    elif a == 3.0:
        print('B')
    elif a == 3.3:
        print('B+')
    elif a == 3.7:
        print('A-')
    elif a == 4:
        print('A')
    elif a > 4:
        print('A+')
    else:
        print('Такого значення немає у таблиці')
while True:
    a = float(input(''))
    if a == -1:
        break
    elif a == 0 or a == 1 or a == 1.3 or a == 1.7 or a == 2.0 or a == 2.7 or a == 3.0 or a == 3.3 or a == 3.7 or a == 4 or a > 4:
        iff(a)
        b.append(a)
    else:
        print('Error')
s = (sum(b))/len(b)
print(s)
iff(s)



def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

