# I want to create a form for the parents for their
# child meal

import datetime
from datetime import date


title = 'Grădinița Paradisul Copiilor'
print(title)

name = str(input('Nume copil: ')).lower()


surname = str(input('Prenume copil: ')).lower()

group = str(input('Grupa: ')).lower()

today = date.today()

present = str(input('Prezent? '))
if present == 'da'.lower():
    str(input("Tip masă: "))
else:
    exit()




