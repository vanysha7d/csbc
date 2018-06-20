import datetime

print("Вкажіть рівень шуму:")
a=int(input())

if 0<a<40:
    print("Нижче Quiet room")
    
elif a==40:
    print("Quiet room")
    
elif 40<a<70:
    print("Між Quiet room та Alarm clock")
    
elif a==70:
    print("Alarm clock")

elif 70<a<106:
    print("Між Alarm clock та Gas Lawnmower")

elif a==106:
    print("Gas Lawnmower")

elif 106<a<130:
    print("Між Gas Lawnmower та Jackhammer")

elif a==130:
    print("Jackhammer")

elif a>130:
    print("Більше Jackhammer")

elif a<0:
    print("Помилка")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

    
