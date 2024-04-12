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

