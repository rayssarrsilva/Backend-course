# while loop = executa um codigo enquanto a condição for verdadeira

name = input("digite seu nome: ")

if name == "":
    print("voce nao inseriu nenhum nome")
else:
    print(f"ola {name}")

while name == "": 
    print("voce nao inseriu nenhum nome")
    name = input("digite seu nome: ")
print(f"ola {name}")

#-----------------------------------------
# o usuario deve digitar um numero maior que 0, caso contrario ele devera digitar novamente.
age = int(input("digite sua idade: "))

while age < 0:
    print("idade nao pode ser negativa")
    age = int(input("digite sua idade: "))
print(f"voce tem {age} anos de idade")

#-------------------------------------------

#o usuario digita as comidas que gosta, e clica Q para sair do programa e nenhuma mensagem é mostrada após isso.
food = input("coloque a comida que voce gosta (q to quit) ")

while not food == "q":
    print(f"you like {food}")
    food = input("digite outra comida que voce gosta: (q to quit) ")

#----------------------------------------------

num = int(input("digite um numero entre 1 - 10 "))

while num < 1 or num > 10:
    print(f"{num} nao é valido")
    num = int(input("digite um numero entre 1 - 10 "))

print(f"o numero digitado é {num}")