# Lists = [] ordenada, aceita itens duplicados e é mutavel(pode ter valor alterado após a criação).
fruit = ["apple","orange","banana","grapes","melon"]
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[0:3]) #do primeiro ao terceiro
print(fruit[::2]) #pula um item considerado o between
print(fruit[::-1]) #começa de tras pra frente

print(dir(fruit)) #mostra os metodos e atributos disponiveis pra essa lista
#help(fruit), descriçao dos metodos de dir

fruit[0] = "maça" #altera o item 0 da lista fruit pra maça

# insere melancia na posiçao 1 substituindo o item anterior
fruit.insert(1,"melancia")

#insere beans na ultima posiçao
fruit.append("beans")

#remove todos os itens chamado banana
fruit.remove("banana")

#coloca os itens em ordem alfabetica/crescente
fruit.sort()

#mostra a lista de trás pra frente
fruit.reverse()

#mostra a posiçao do item colocado entre parentesses
print(fruit.index("grapes"))
for x in fruit:
    print(x) #iterando entre os itens da lista
#----------------------------------------------------
#set = {} desordenado e imutavel, mas aceita add e remove. sem duplicaçoes

fruits = {"apple","orange","banana","grapes","melon"}
#print(dir(fruits)) #mostra metodos, funçoes e atributos disponiveis
#print(help(fruits)) #detalha o dir

#metodo que adiciona itens 
print(fruits.add("pineapple"))
#metodo que remove itens
print(fruits.remove("apple"))
#remove o primeiro item aleatoriamente
#print(fruits.pop())
print(fruits)
#-----------------------------------------------------
# tupla = () ordenada e unchangeable. duplicaçoes sao aceitas

frutas = ("apple","orange","banana","grapes","melon")
#dir, help, len, in. metodos disponiveis: index e count. 
