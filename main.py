print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")

condicao1 = input('Para qual lado deseja ir? Escolha "esquerda" ou "direita": ').lower()
if condicao1 == "esquerda":
    condicao2 = input('Você chegou em um lago, há uma ilha no meio do lago. Digite "esperar" para aguardar um barco ou "nadar" para atravessar nadando. ').lower()
    if condicao2 == "esperar":
        door = input('Você chegou na ilha e se deparou com 3 portas na sua frente e em uma delas esta o tesouro. Qual porta você deseja abrir? "vermelha" ou "amarela" ou "azul". ').lower()
        if door == "amarela":
            print("Parábens! Você ganhou e encontrou o tesouro!!!!!!!!!!!")
        elif door == "vermelha": 
            print("Queimado pelo fogo! Game over.")
        elif door == "azul":
            print("Comido pelas bestas! Game over.")
        else:
            print("Game over.")
    else:
        print("Você foi atacado por uma truta zangada.Game over.")
else: 
    print("Você caiu em um buraco. Game over!")