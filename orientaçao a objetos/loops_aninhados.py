# loops aninhados = loops com outro loop dentro
#  outer loop:
#    inner loop:

for x in range(1,10):
    print(x, end=" ") #printa de 1 a 10 na mesma linha com espaço entre si

for x in range(3): #qualquer coisa dentro desse loop será repetida 3x
    for y in range(1,10):
        print(y, x) #mostra os valores do range de Y e em qual repetiçao ele se encontra na variavel X

for a in range(2): #repete o for do b duas vezes 
    for b in range(1,11): 
        print(b, end=" ") # mostra os valores que b irá iterar na mesma linha com um espaço
    print() # da um espaço cada vez que o inner loop for completado

#----------------------------------------
rows = int(input("digite o numero de linhas: "))
columns = int(input("digite o numero de colunas: "))
symbol = input("digite um simbolo: ")

for c in range(rows):
    for d in range(columns):
        print(symbol, end="")
    print()



