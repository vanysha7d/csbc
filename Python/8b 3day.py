import datetime

c = {'A' : '.-', 'B' : '-...', 'C' : '-.-.',
     'D' : '-..', 'E' : '.', 'F' : '..-.',
     'G' : '--.', 'H' : '....', 'I' : '..',
     'J' : '.---', 'K' : '-.-', 'L' : '.-..',
     'M' : '--', 'N' : '-.', 'O' : '---',
     'P' : '.--.', 'Q' : '==.-', 'R' : '.-.',
     'S' : '...', 'T' : '-', 'U' : '..-',
     'V' : '...-', 'W' : '.--', 'X' : '-..-',
     'Y' : '-.--', 'Z' : '--..', '0' : '-----',
     '1' : '.----', '2' : '..---', '3' : '...--',
     '4' : '....-', '5' : '.....', '6' : '-....',
     '7' : '--...', '8' : '---...', '9' : '----.'}
a = input("Введіть символи для перетворення в мову морзе: ").upper()
b = ""


for i in a:
  if i in c:
    b += c[i] + " "
  else:
    b += " "
    
print("Ваш код в морзе: ")
print(b)


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іванченко Іван та Балацький Олександр"

printTimeStamp(name)

