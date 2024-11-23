'''
Atividade 1 - Dada a seguinte lista de frutas:

frutas = ["maçã", "banana", "laranja", "uva"]

Imprima cada fruta da lista utilizando o for, uma de cada vez.
'''
# frutas = ["maçã", "banana", "laranja", "uva"]
# for fruta in frutas:
#     print(fruta)


'''
Atividade 2 - Lista de tarefas:

tarefas = ["Arrumar a cama", "Tomar café", "Estudar", "Jogar videogame"]

Escreva um programa que diga:

"Tarefa: nome da tarefa" para cada tarefa da lista.
'''
# tarefas = ["Arrumar a cama", "Tomar café", "Estudar", "Jogar videogame"]
# for tarefa in tarefas:
#     print('Tarefa: ', tarefa)


'''
Atividade 3 - Imprimindo letras de uma palavra

palavra = 'python'

Escreva um código que imprima cada letra da palavra, uma por vez.
'''
# palavra = 'python'
# for letra in palavra:
#     letra = letra.strip()
#     print(letra)


'''
Atividade 4 - Dividindo frases

frase = "Estou estudando python"

Escreva um programa que imprima cada PALAVRA da frase em uma linha.

Dica: Use o método .split()
'''
# frase = "Estou estudando python"
# palavras = frase.split()
# for palavra in palavras:
#     print(palavra)


'''
Atividade 5 - Contando até 10

Use o range para imprimir os números de 1 a 10.
'''
# for x in range(1,11):
#     print(x)


'''
Atividade 6 - Tabuada

Escreva um programa que imprima a tabuada do 9.
'''
# numero = 9
# for x in range(1,11):
#     mult = numero*x
#     print(f'{numero} X {x} = {mult}')


'''
Atividade 7 - Contagem Regressiva

Faça uma contagem regressiva de 10 até 1.
No final imprima: Feliz ano novo!
'''
# for x in range(10,0,-1):
#     print(x)


'''
Atividade 8 - Somando números

Calcule a soma de todos os números de 1 a 100 e mostre o resultado.

Dica: Use uma variável para acumular a soma.
'''
# soma = 0
# for x in range(1,101):
#     soma = soma + x
# print(soma)


'''
Atividade 9 - Listando números pares

Imprima todos os números pares de 2 a 20.
'''
# for x in range(2,21,2):
#     print(x)


'''
Atividade 10 - Quadrado dos números

Imprima o quadrado dos números de 1 a 10.

Exemplo: 2 x 2 = 4

Dica: Multiplique cada número por ele mesmo.
'''
# mult = 0
# indice = 0
# for x in range(1,11):
#     indice = indice + 1
#     mult = x*x
#     print(f'O numero {indice} tem seu quadrado sendo {mult}.')


'''
Atividade 11 - Verificando a idade mínima

Você está organizando uma festa, mas só pode convidar pessoas com 18 anos ou mais.

Use o range para gerar idades de 10 a 20 e imprima se a idade é permitida ou não:
"Idade 10: Não pode entrar"
"Idade 18: Pode entrar!"
'''
# for idade in range(10,21):
#     if idade < 18:
#         print('Idade ',idade,': Não pode entrar.')
#     else:
#         print('Idade ',idade,': Pode entrar')


'''
Atividade 12 - Pulando Números

Use o range para imprimir apenas os números que terminam em 5 entre 5 e 50.

Exemplo: 5, 15, 25...
'''
# for x in range(5,50,10):
#     print(x)


'''
Atividade 13 - Encontrando itens com indices

Faça um programa que percorra uma lista de compras e mostre o índice de cada
item junto com seu nome.
'''
# lista = ['Arroz','Feijão','Carne','Sabão','Macarrão','Óleo']
# for indice, item in enumerate(lista, start=1):
#     print(f'{indice} - {item}')


'''
Atividade 14 - Encontrando o maior número

Percorra uma lista de números usando enumerate e informe qual número é o maior
e em qual posição ele está.
'''
# lista = [1,3,10,4,26,2,40,5,23]
# maior = max(lista)
# for indice, numero in enumerate(lista):
#     if maior == numero:
#         print(f'O maior número é {numero} e sua posição é {indice}')


'''
Atividade 15 - Posicionando palavras

Percorra uma frase e mostre o índice de cada palavra.

frase = "Aprender Python é massa"
'''
# frase = "Aprender Python é massa"
# palavra = frase.split()
# for indice, palavra in enumerate(palavra, start=1):
#     print(f'A palavra {palavra} está na posição {indice}')


'''
Atividade 16 - Verificando a presença de um item

Dada uma lista de alunos, encontre a posição de um aluno específico.

alunos = ["João", "Maria", "Pedro", "Ana"]
aluno_procurado = "Pedro"
'''
# alunos = ["João", "Maria", "Pedro", "Ana"]
# procurado = "Pedro"
# print(f'O aluno procurado é o Pedro e sua posição é {alunos.index("Pedro")}')

# for indice, aluno in enumerate(alunos):
#     if aluno == procurado:
#         print(f'O aluno procurado é o {procurado} e sua posição é {indice}')



'''
Atividade 17 - Conferindo tarefas

Percorra uma lista de tarefas e mostre quais já foram feitas e quais ainda não
foram feitas.

tarefas = ["Lavar a louça", "Estudar", "Jogar videogame"]
status = [True, False, True]
'''
# tarefas = ["Lavar a louça", "Estudar", "Jogar videogame"]
# status = [True, False, True]
# for tarefa in range(len(tarefas)):
#     for feito in range(len(status)):
#         if tarefa == feito:
#             print(f'{tarefas[tarefa]} - {status[feito]}')


'''
Atividade 18 - Conferindo estoque

Percorra uma lista de produtos e exiba a quantidade de cada um no estoque.

produtos = ["Banana", "Maçã", "Laranja", "Uva"]
quantidades = [10, 5, 7, 3]
'''
# produtos = ["Banana", "Maçã", "Laranja", "Uva"]
# quantidades = [10, 5, 7, 3]
# for produto in range(len(produtos)):
#     for quant in range(len(quantidades)):
#         if produto == quant:
#             print(f'{produtos[produto]} - {quantidades[quant]}')


'''
Atividade 19 - Calculando desconto progressivo

Uma loja dá descontos progressivos em produtos: 10% no 1º produto,
20% no 2º e assim por diante. Calcule o preço final de cada produto com
base na lista de preços.

precos = [100, 200, 300, 400, 500]
'''
# precos = [100, 200, 300, 400, 500]
# for indice, preco in enumerate(precos, start=1):
#     desconto = indice*10
#     final = preco - (preco*(desconto/100))
#     print(f'Produto {indice} tem como preço original {preco} e preço final {final}')


'''
Atividade 20 - Encontrando múltiplos de 3

Dada uma lista de números, encontre os índices de todos os múltiplos de 3.

numeros = [5, 9, 12, 7, 15, 22, 18]
'''
# numeros = [5, 9, 12, 7, 15, 22, 18]
# for indice, num in enumerate(numeros):
#     if num%3 == 0:
#         print(f'Os números {num} são multiplos de 3 e estão na posição {indice}')


'''
Atividade 21 - Verificação de palíndromos

Dada uma lista de palavras, identifique quais são palíndromos
(lê-se igual de trás para frente).

palavras = ["arara", "python", "radar", "palavra", "ana"]
'''
# palavras = ["arara", "python", "radar", "palavra", "ana"]
# for palavra in palavras:
#     if palavra == palavra[::-1]:
#         palin = palavra
#         print(f'A palavra {palin} é um palindromo')


'''
Atividade 22 - Classificando temperaturas

Dada uma lista de temperaturas em graus Celsius, categorize-as como "frio",
"agradável" ou "quente".

Frio: abaixo de 15°C
Agradável: entre 15°C e 25°C
Quente: acima de 25°C

temperaturas = [10, 18, 22, 30, 5, 15, 25]
'''
# temperaturas = [10, 18, 22, 30, 5, 15, 25]
# for temp in temperaturas:
#     if temp <= 15:
#         print(f'A temperatura {temp} é classificada como frio.')
#     if temp>15 and temp<=25:
#         print(f'A temperatura {temp} é classificada como agradável.')
#     if temp > 25:
#         print(f'A temperatura {temp} é classificada como calor.')


'''
Atividade 23 - Contando letras repetidas

Conte quantas vezes cada letra aparece em uma palavra e exiba o resultado.

palavra = "banana"
'''
cont = 0
palavra = "banana"
letra = palavra.split()
for letra in palavra:
    iguais = letra == letra[:-1]
    print(iguais)
    # print(letra)
    # if letra == iguais :
    #     cont = cont + 1
    #     print(f' A letra {letra} aparece {cont}')