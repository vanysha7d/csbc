﻿import winsound
import datetime

j = [(440,500), (440,500), (440,500), (349,350), (523,150), (440,500), (349,350),
(523,150), (440,1000), (659,500), (659,500), (659,500), (698,350), (523,150),
(415,500), (349,350), (523,150), (440,1000)]
for i in range(len(j)):
    winsound.Beep(j[i][0], j[i][1])


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

