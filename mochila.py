#pip install playsound==1.2.2
#pip install art==5.6
#pip install tqdm

#from playsound import playsound as som
from art import text2art as textArte
import datetime as dt
from tqdm import tqdm
from time import sleep
import os

def assetArt(art):
    draw = open(art, "r", encoding="utf8")
    print(''.join([line for line in draw]))

os.system('clear')

print(textArte("Python Adventures", font="slant"))
print(textArte("Backpack Creator", font="slant"))
print("\n")

load = 0

dOWeek = dt.datetime.today().weekday()
days = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
dOWeek = days[dOWeek]
if dOWeek != "Sábado" and dOWeek != "Domingo":
    print(f"Tenha uma ótima {dOWeek}!\n")
else:
    print(f"Tenha um ótimo {dOWeek}!\n")
sleep(1)

charExists = 0

personagensCadastradas = []
if not os.path.exists("characters"):
    print("Diretório de personagens não encontrado.")
    sleep(2)
    for i in tqdm(range(0,100), desc="Criando diretório de personagens", ascii=True):
        sleep(.005)
    os.mkdir('characters')
    print("Diretório de personagens criado!\n\n")

if len(os.listdir("characters")) == 0:
    charExists = 0
else:
    charExists = 1

if charExists == 0:
        while True:
            opc = input("Deseja criar um personagem para usar o programa? (s/n) -> ").lower()
            if opc == "s":
                load = False
                break
            elif opc == "n":
                print("\nObrigado por usar Python Adventures Backpack Creator!")
                sleep(2)
                exit()
            else:
                continue
else:
    load = False
    while True:
        opc = input("Escolha uma das opções disponíveis\nc - Criar um novo personagem | l - Carregar um personagem existente | q - Sair do programa\n-> ").lower()
        if opc == "c":
            break
        elif opc == "l":
            sleep(1)
            os.system('clear')
            print(textArte("Load Character", font="cybermedium"))
            personagensCadastradas.extend(os.listdir('characters'))
            for i in tqdm(range(0,100), desc="Carregando personagens", ascii=True):
                sleep(.01)
            print(f"\nPersonagens:\n")
            for i,e in enumerate(personagensCadastradas):
                print(f"{i} - {e[0:-4]}")
            print("")
            while True:
                opc = input("Digite o número do personagem que deseja carregar -> ")
                if opc == "":
                    continue
                elif opc.isdigit() and int(opc) <= len(personagensCadastradas)-1 and int(opc) >= 0:
                    load = True
                    save = personagensCadastradas[int(opc)]
                    break
                else:
                    continue
            break
        elif opc == "q":
            print("\nObrigado por usar Python Adventures Backpack Creator!")
            sleep(2)
            exit()

if not load:
    sleep(1)
    os.system('clear')
    print(textArte("Character Creation", font="cybermedium"))
    while True:
        nome = input("Digite o nome do personagem\n-> ")
        if nome == "":
            continue
        nome = nome+".txt"
        if os.path.exists(f"characters/{nome.lower()}"):
            print("Personagem já existe!")
            continue
        else:
            while True:
                opc = input("Escolha a classe do personagem\ng - Guerreiro | m - Mago\n-> ").lower()
                if opc == "g":
                    classe = "Guerreiro"
                    break
                elif opc == "m":
                    classe = "Mago"
                    break
                else:
                    continue
            with open(f"characters/{nome.lower()}", "w") as char:
                for i in tqdm(range(0,100), desc=f"Criando {nome[0:-4]}", ascii=True):
                    sleep(.006)
                char.write(f"personagem//Classe//{classe}\narmas//Espada longa//dano//1d8//valor//15po//peso//1,5k\narmaduras//Couro//ca//1//valor//10po//peso//5kg\nequipamentos//Mochila//Corda de Escalada//Barraca//Bussola\ndinheiro//5PO//5PP//5PC\n")
            print("O personagem será criado com o equipamento inicial")
            sleep(.5)
            print(f"{nome[0:-4]} criado com sucesso!")
            save = nome.lower()
            break

sleep(2)
os.system('clear')
for i in tqdm(range(0,100), desc="Carregando informação de personagem", ascii=True):
    sleep(.01)
sleep(1)

charBackpack = {}

with open(f"characters/{save}", "r", encoding="utf8") as file:
    txt = [data[0:-1] for data in file.readlines()]
    for e in txt:
        pato = e.split("//")
        charBackpack[pato[0]] = pato[1:]
    """ for k,v in charBackpack.items():
        charBackpack[k] = {v[0]:v[1:]} """

#print padrao de personagem
def printPadrao():
    os.system('clear')
    print(textArte(f"{save[0:-4]}", font="cybermedium"))
    print(f"Classe: {charBackpack['personagem'][1]}\n")


sair = False
#apagar - adicionar - editar - visualizar - pesquisar
while True:
    printPadrao()
    print(f"{'=-'*30}")
    while True:
        opc = input("Escolha uma das opções disponíveis\nd - apagar | a - adicionar | e - editar | v - visualizar | s - pesquisar | q - sair\n-> ").lower()
        if opc == "d":
            break
        elif opc == "a":
            break
        elif opc == "e":
            break
        elif opc == "v":
            break
        elif opc == "s":
            break
        elif opc == "q":
            break
        else:
            continue
    if opc == "d":
        pass
    elif opc == "a":
        while True:
            ask = input("Escolha a categoria do item que você deseja adicionar\nw - Armas | a - Armadura | e - Equipamento | m - Dinheiro\n-> ").lower()
            if ask == "w":
                add = "armas"
                catID = 1
                break
            elif ask == "a":
                add = "armaduras"
                catID = 2
                break
            elif ask == "e":
                add = "equipamentos"
                catID = 3
                break
            elif ask == "m":
                add = "dinheiro"
                catID = 4
                break
            else:
                continue
        
        nomeItem = input("Digite o nome do item -> ").capitalize()
        propItem = input("Digite a propriedade do item").lower()
        with open(f"characters/{save}","r") as arquivo:
            print(arquivo)
            txt = [data[0:-1] for data in arquivo.readlines()]
            txt[catID]+=f"//{nomeItem}//{propItem}"
            print(txt)
            txt= "\n".join(txt)
            with open(f"characters/{save}","w") as file:
                file.write(txt)
            
            
    elif opc == "e":
        pass
    elif opc == "v":
        charBackpack = {}

        with open(f"characters/{save}", "r", encoding="utf8") as file:
            txt = [data[0:-1] for data in file.readlines()]
            for e in txt:
                pato = e.split("//")
                charBackpack[pato[0]] = pato[1:]
        print("Abrindo a mochila do personagem...")
        sleep(1)
        assetArt("assets/art/backpack.txt")
        for i in tqdm(range(0,100), desc="Abrindo mochila", ascii=True):
            sleep(.001)
        #som("assets/audio/zipperaudio.mp3")
        print("Mochila aberta!")
        sleep(1)
        os.system('clear')

        printPadrao()
        print(f"{'=-'*30}")
        

        print("Armas\n")
        for i,e in enumerate(charBackpack['armas']):
            if i == 0:
                print(e)
            elif i %2 != 0:
                print(f"{charBackpack['armas'][i]} | {charBackpack['armas'][i+1]}")
            
        print(f"{'=-'*30}")

        print("Armaduras\n")
        for i,e in enumerate(charBackpack['armaduras']):
            if i == 0:
                print(e)
            elif i %2 != 0:
                print(f"{charBackpack['armaduras'][i]} | {charBackpack['armaduras'][i+1]}")
        print(f"{'=-'*30}")

        print("Equipamentos\n")
        for i,e in enumerate(charBackpack['equipamentos']):
            print(e)
        print(f"{'=-'*30}")

        print("Dinheiro\n")
        for i,e in enumerate(charBackpack['dinheiro']):
            print(e)
        print(f"{'=-'*30}")

        while True:
            opc = input("Digite (q) para voltar -> ").lower()
            if opc == "q":
                break
            else:
                continue
    elif opc == "s":
        pass
    elif opc == "q":
        print("\nObrigado por usar Python Adventures Backpack Creator!")
        sleep(2)
        exit()