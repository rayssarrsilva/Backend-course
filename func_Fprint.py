def is_bob(nome):
    return nome.lower() == "bob"
# retorna algo apenas se o nome inserido por bob em minusculo
if is_bob("rayssa"):
    print(f"voce se chama bob e nao pode entrar aqui")

def main():
    is_bob("bob")

if __name__ == '__main__':
    main()
#---------------------------

n: int = 1000000000

#separa a cada tres casas, só há essas duas opçoes
print(f"{n:,}")
print(f"{n:_}")

var = 'var'
print(f'{var:>20}:') #da um espaço de 20 linhas ate iniciar a variavel
print(f'{var:^20}') #deixa a variavel na metade do numero 20
print(f'{var:_>20}') #coloca traço pra dar espaço

n = 122342234234
print(f'{n:.2f}') #da um espaço de tras pra valor, com o valor que for inserido
print(f'{n:,.3f}') #coloca virgula e ponto

a = 123445
b = 892313
print(f'{a + b = }') #mostra a soma sem calculo prévio
