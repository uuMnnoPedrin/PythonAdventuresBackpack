#pip install playsound
#pip install art==5.6

from playsound import playsound as som
from art import text2art as textArte
import datetime as dt
import os

os.system('clear')
#print(textArte("Python Adventures: Backpack DLC", font="slant"))
print("\n")
dOWeek = dt.datetime.today().weekday()
if dOWeek == 1:
    print("Olá,\nTenha uma boa segunda-feira!")
elif dOWeek == 2:
    print("Olá,\nTenha uma boa terça-feira!")
elif dOWeek == 3:
    print("Olá,\nTenha uma boa quarta-feira!")
elif dOWeek == 4:
    print("Olá,\nTenha uma boa quinta-feira!")
elif dOWeek == 5:
    print("Olá,\nTenha uma boa sexta-feira!")
elif dOWeek == 6:
    print("Olá,\nTenha uma boa sabado!")
elif dOWeek == 0:
    print("Olá,\nTenha uma boa domingo!")
    

personagensCadastradas = []
personagensCadastradas.extend(os.listdir('characters'))
print(personagensCadastradas)