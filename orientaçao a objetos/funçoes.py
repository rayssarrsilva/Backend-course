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