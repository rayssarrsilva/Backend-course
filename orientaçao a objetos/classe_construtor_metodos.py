#No Python, todas as classes devem, por boas práticas, possuir nomes que comecem com letra maiúscula e
#caso sejam compostos, a primeira letra de cada palavra deve ser maiúscula, o que chamamos de formato CamelCase.

#criando a classe pessoa
class pessoa():
    #criando o construtor da classe pessoa e declarando os atributos dentro da classe
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf  = cpf

class pessoa2():
    #construtores padrao tem init o resto nao precisa
    def __init__(self, idade, signo):
        self.idade = idade
        self.signo = signo

#instanciando objeto
if __name__== "__main__":
    objeto1 = pessoa("ray", "F", 123445)

#ao instanciar é necessario adicionar as informaçoes dentro do parenteses. 
if __name__=="__main__":
    objeto2 = pessoa2(18, "leao")
    print(objeto2.idade, objeto2.signo)

#ao se referir ao atributo especifico é necessario utilizar o objeto e o atributo especificados
objeto1.cpf = 123455
print(objeto1.cpf)
objeto1.nome = "rayssa roberta"
print(objeto1.nome)
objeto1.sexo = "F"
print(objeto1.sexo)

#declarando métodos
class Pessoa:
    #atributos do construtor
    def __init__(self, nome, sexo,cpf,ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    #metodo 
    def desativar(self):
        self.ativo = False 
        print("A pessoa foi desativada com sucesso")

#instanciando
if __name__ == "__main__":
    pessoaA = Pessoa("ray","F","123456", True)
    #ao puxar o metodo com o objeto, caso ele ja possua print nao é necessario chamar print.
    pessoaA.desativar()

#declarando propriedades

 # Utilizando properties
    pessoaA.nome = "José"
    print(pessoaA.nome)

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