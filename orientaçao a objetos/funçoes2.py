# Ao chamar uma função, indicamos somente os valores com os quais ela vai operar
def soma(a, b):
    resultado = a+b
    return resultado

print(soma(123412,5234))
#Se adicionarmos um parâmetro na criaçao da função, ao chamá-la teremos que inserir um argumento
def ola_mundo(nome):
    print("bem vindo ao terminal do python",nome,"!")

ola_mundo("rayssa")

#parametro Nomeado (não importa a ordem)
print(soma(a=12, b=14))

#parametro Posicional (a ordem importa)
print(soma(123123, 345345))

#para adicionar um parametro que pode ser chamado infinitas vezes adicione asterisco
def cadastro(*nome):
    print("ola",nome,"!")

cadastro("rayssa", "luiza", "clara", "julia", "ana")

def calculo(a,b):
    resultado = a - b
    return resultado #usado geralmente pra calculos

calculo(8123, 123)

#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def minha_funçao(**parametro):
    print("seu ultimo nome é " + parametro["fname"]) #o que for colocado entre aspas irá aparecer

minha_funçao(fname = "silva", nome="luisa", nome1="clara")

#deixa um parametro padrao caso nada seja inserido
def nome(padrao = " *insira um nome*"):
    print("meu nome é" + padrao)

nome()
nome("ray")

#Passing a List as an Argument
def funçao(food):
    for q in food:
        print(q)

frutas = ["maça","uva","melancia"]
funçao(frutas) #mostra apenas as palavras da lista

#teste 2
def fun2(food):
    print(food)

print(frutas) #mostra a lista sem alteraçoes

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = "keyword")

#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d): #2 posicionais e 2 keyword
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


