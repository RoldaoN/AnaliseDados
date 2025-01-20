'''
Atividade 1

Crie uma função chamada calcular_gorjeta que receba o valor de
uma conta e a porcentagem da gorjeta desejada. A função deve
retornar o valor total (conta + gorjeta).
'''
# def calcularGorjeta (valor,porcent):
#     result = valor + (valor*(porcent/100))
#     print(f'O valor da conta ficou de {result:.2f}')
# conta = float(input('Entre com o valor da conta: '))
# porcent = float(input('Qual a porcentagem da gorjeta? '))
# calcularGorjeta(conta,porcent)


'''
Atividade 2

Crie uma função chamada celsius_para_fahrenheit que converta
uma temperatura de Celsius para Fahrenheit. Use a fórmula:
F = C * 9/5 + 32.
'''
# def conversao (temp):
#     f = (temp*(9/5))+32
#     print(f'A temperatura de {temp} é igual a {f:.2f} Fahrenheit')
# celsius = float(input('Entre com a temperatura em Celsius: '))
# conversao(celsius)


'''
Atividade 3

Crie uma função chamada quantidade_total que receba uma lista
com quantidades de itens (por exemplo, [2, 3, 5]) e some tudo.
'''
# def quantTotal (lista):
#     for x in lista:
#         total = sum(lista)
#         return total 
# lista = [2,3,5]
# total = quantTotal(lista)
# print(f'O resultado da soma é {total}')


'''
Atividade 4

Crie uma função chamada verificar_maioridade que receba uma
idade e retorne "Maior de idade" se a pessoa tiver 18 anos ou
mais, ou "Menor de idade" caso contrário.
'''
# def maiorIdade(idade):
#     if idade >= 18:
#         print(f'Você é maior de idade.')
#     else:
#         print(f'Você é menor de idade.')
# idade = int(input('Qual a sua idade? '))
# maiorIdade(idade)


'''
Atividade 5

Crie uma função chamada calcular_desconto que receba o preço de
um produto e a porcentagem de desconto. Retorne o preço com o
desconto aplicado.
'''
# def calculaDesconto(valor,desconto):
#     result = valor-(valor*(desconto/100))
#     print(f'O valor do produto com o desconto informado é de {result:.2f}')
# preco = float(input('Digite o preço do produto: '))
# porcento = float(input('Digite a porcentagem de desconto: '))
# calculaDesconto(preco,porcento)


'''
Atividade 6

Crie uma função chamada contar_palavras que receba uma frase e
diga quantas palavras ela tem.
'''
# def contaPalavra(frase):
#     for indice, valor in enumerate(frase.split()):
#         indice += 1

#     print(f'O total de palavras é {indice}')
# frase = input('Digite uma frase: ')
# contaPalavra(frase)

'''
Atividade 7

Crie uma função chamada revisar_texto que receba um texto e uma
palavra. A função deve contar quantas vezes a palavra aparece
no texto.
'''
# def revisaTexto(texto,palavra):
#     num = 0
#     for p in range(len(texto)):
#         if texto[p:p + len(palavra)] == palavra:
#             num += 1
#     return num
# texto = input('Digite o texto: ')
# palavra = input('Digite uma palavra para verifica-la no texto: ')
# numero = revisaTexto(texto,palavra)
# print(f'A palavra {palavra} aparece {numero} vezes no texto')


'''
Atividade 8

Crie uma função chamada calcular_tempo_viagem que receba a
distância em km e a velocidade média em km/h. Retorne o tempo
estimado de viagem em horas.
'''
# def tempoViagem(distancia,tempo):
#     result = distancia//tempo
#     print(f'A viagem vai demorar em média {result} horas')

# km = float(input('Qual a distância que será percorrida? '))
# velo = float(input('Qual a velocidade média usada? '))
# tempoViagem(km,velo)


'''
Atividade 9

Crie uma função chamada par_ou_impar que receba um número e
retorne se ele é "Par" ou "Ímpar".
'''
# def parImpar(numero):
#     if (numero%2) == 0:
#         print(f'O numero {numero} é par.')
#     else:
#         print(f'O número {numero} é impar')
# numero = float(input('Digite um número para verificar se ele é par ou impar: '))
# parImpar(numero)


'''
Atividade 11

Crie uma função chamada calcular_comissao que calcule a comissão
de um vendedor, levando em consideração o valor total das vendas.
Se o valor das vendas for superior a R$ 10.000, a comissão será
de 8%, caso contrário será 5%.
'''
# def calculoComissao(valor):
#     if valor >= 10000:
#         result = valor*(8/100)
#         print(f'O valor da comissão será de {result:.2f}')
#     else:
#         result = valor*(5/100)
#         print(f'O valor da comissão será de {result:.2f}')
# comissao = float(input('Digite o valor da venda para ver a comissão do vendedor: '))
# calculoComissao(comissao)


'''
Atividade 12

Crie uma função chamada converter_temperatura que receba uma
temperatura e o tipo de conversão desejada (Celsius para
Fahrenheit, Celsius para Kelvin, Fahrenheit para Celsius, etc.).
Use um parâmetro adicional para determinar a conversão.
'''
# def conversaoTemp(valor):
#     escolha = int(input('A temperatura digitada está em:\n1 - °Celcius\n2 - °Fahrenheit\n3 - °Kelvin\n'))
#     transforma = int(input('Agora deseja tranformar ela em:\n1 - °Celcius\n2 - °Fahrenheit\n3 - °Kelvin\n'))
#     if escolha == 1 and transforma == 2:
#         cF = (valor*(9/5))+32
#         print(f'A temperatura de {temp}°C é igual a {cF:.2f}°Fahrenheit.')
#     elif escolha == 1 and transforma == 3:
#         cK = valor + 273.15
#         print(f'A temperatura de {temp}°C é igual a {cK:.2f}°Kevin.')
#     elif escolha == 2 and transforma == 1:
#         fC = 5/9*(valor-32)
#         print(f'A temperatura de {temp}°Fahrenheit é igual a {fC:.2f}°C.')
#     elif escolha == 2 and transforma == 3:
#         fK = (temp - 32)*(5/9)+273.15
#         print(f'A temperatura de {temp}°Fahrenheit é igual a {fK:.2f}°Kelvin.')
#     elif escolha == 3 and transforma == 1:
#         kC = temp - 273.15
#         print(f'A temperatura de {temp}°Kelvin é igual a {kC:.2f}°C.')
#     else:
#         kF = (temp - 273.15)*(9/5)+32
#         print(f'A temperatura de {temp}°Kelvin é igual a {kF:.2f}°C.')
# temp = float(input('Digite a temperatura desejada: '))
# conversaoTemp(temp)


'''
Atividade 13

Crie uma função chamada calcular_media_ponderada que receba três
notas e seus respectivos pesos. A função deve retornar a média
ponderada.
'''
# def mediaPondera():
#     nota1 = 0
#     peso1 = 0
#     total = 0
#     nota = 0
#     peso = 0
#     while True:
#         nota = float(input('Digite a nota ou escreva 11 para sair.\n'))
#         if nota == 11:
#             break
#         peso = float(input('Digite o peso da prova de 1 a 10 ou 11 para sair.\n'))
#         if peso == 11:
#             break
#         if nota != 11 or peso != 11:
#             nota1 += nota * peso
#             peso1 =peso1 + peso
#         else:
#             break
#     total = nota1/peso1
#     print(f'A media ponderada das notas informadas é de {total:.2f}')
# mediaPondera()


'''
Atividade 14

Crie uma função chamada contar_caracteres que receba um texto e
uma lista de caracteres. A função deve contar quantas vezes cada
um dos caracteres aparece no texto.
'''
# def contaCaracter(texto):
#     texto1 = texto.strip()
#     for indice, letra in enumerate(texto1):
#         indice +=1
#     print(f'A quantidade de caracteres é de {indice}')
# texto = input('Digite um texto: ')
# contaCaracter(texto)


'''
Atividade 15

Crie uma função chamada verificar_primo que verifique se um
número é primo ou não. Um número é primo se for maior que 1 e
não puder ser dividido por nenhum outro número, exceto por 1 e
ele mesmo.
'''
# def verificaPrimo(valor):
#     if valor > 1:
#         for x in range(2,valor):
#             if valor%x == 0:
#                 print(f'O número {valor} não é primo.')
#                 break
#             else:
#                 print(f'O número {valor} é primo.')
#                 break
# numero = int(input('Digite um número: '))
# verificaPrimo(numero)


'''
Atividade 16

Crie uma função chamada calcular_fatorial que calcule o fatorial
de um número inteiro (fatorial de n é o produto de todos os
números de 1 até n).
'''
# def fatorial (valor):
#     fator = 1
#     while valor != 0:
#         fator = fator*valor
#         valor -= 1
#     print(fator)
# numero = int(input('Digite um número para ser fatorado: '))
# fatorial(numero)


'''
Atividade 17

Crie uma função chamada media_notas que receba um dicionário com
os nomes dos alunos e suas respectivas notas em uma lista. A
função deve calcular a média das notas de cada aluno e retornar
um novo dicionário com o nome do aluno e sua média.

alunos = {"João": [7, 8, 9], "Maria": [10, 9, 8], "Carlos": [6, 5, 7]}
'''
# alunos = {"João": [7, 8, 9], "Maria": [10, 9, 8], "Carlos": [6, 5, 7]}
# def mediaNotas (valor):
#     somaJoao = sum(alunos['João'])
#     mediaJoao = somaJoao/3
#     somaMaria = sum(alunos['Maria'])
#     mediaMaria = somaMaria/3
#     somaCarlos = sum(alunos['Carlos'])
#     mediaCarlos = somaCarlos/3
#     alunos['João'] = mediaJoao
#     alunos['Maria'] = mediaMaria
#     alunos['Carlos'] = mediaCarlos
#     print(alunos)
# mediaNotas(alunos)


'''
Atividade 18

Crie uma função chamada tabela_multiplicacao que receba um
número e retorne uma função que, quando chamada, mostre a tabela
de multiplicação desse número (de 1 a 10).
'''
# def tabuada(valor):
#     for x in range(1,11):
#         mult = valor*x
#         print(f'{valor} X {x} = {mult}')
# valor = int(input('Digite o número ao qual deseja ver a tabuada: '))
# tabuada(valor)


'''
Atividade 19

Crie uma função chamada reverter_palavras que receba uma frase
e retorne a mesma frase com as palavras em ordem invertida.
A função não deve usar métodos prontos como split() ou join().
'''
def revertePalavra(frase):
    frase1 = frase[::-1]
    print(frase1)
frase = input('Digite uma frase para vê-la ao contrário: ')
revertePalavra(frase)


'''
Atividade 20

Crie uma função chamada numero_espelho que receba dois números
inteiros positivos e verifique se o segundo número é o "espelho"
do primeiro. Um número é espelho do outro se os dígitos de um
estão na ordem inversa do outro.
'''
def numeroEspelho(valor1,valor2):
    if valor1 == valor2[::-1]:
        print(f'O número {valor2} é um número espelho de {valor1}')
    else:
        print('Desculpe os números indicados não são número Espelho.')
valor1 = input('Digite o primeiro número: ')
valor2 = input('Digite no sehundo número ao qual deseja ver se é espelho do primeiro: ')
numeroEspelho(valor1,valor2)