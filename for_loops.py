# é possivel iterar em: range, string, sequence, etc
# for loops = executa blocos de codigo em uma quantidade de vezes fixa

for couter in range(1,11):
    print(couter) #itera de 1 a 10

for x in reversed(range(1,11)):
    print(x) #começa a iterar de tras pra frente

for y in range(1, 11, 2):
    print(y) #conta pulando por 2 números

credit_card = "1234-5678-9012-3456"
#imprime x na quantidade de itens que tem em credit_card na variavel xe imprime todos os itens de credit_card na variavel b.
for b in credit_card:
    print(x, b) 

for c in range(1,21):
    if c == 13:
        continue #pula o numero 13 e vai ate o 20
    else:
        print(c) #mostra todos os valores exceto 13

for d in range(1,21):
    if d == 13:
        break #para o codigo no numero 13 
    else:
        print(d)
