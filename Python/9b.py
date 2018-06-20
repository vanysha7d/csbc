import datetime

print("Введіть номер:")
a=input()

letters = ["A","B","C","D","E","F","G","H","I","j","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

if len(a)== 6:
    if a[0] in letters and a[1] in letters and a[2] in letters and a[3] in numbers and a[4] in numbers and a[5] in numbers:
        print("Підходить старому формату")
    else:
        print("Помилка")
elif len(a)== 7:
    if a[0] in letters and a[1] in letters and a[2] in letters and a[3] in letters and a[4] in numbers and a[5] in numbers and a[6] in numbers:
        print("Підходить новому формату")
    else:
        print("Помилка")
else:
    print("Помилка")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

