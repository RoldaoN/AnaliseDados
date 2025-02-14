# -*- coding: utf-8 -*-
"""prova_pratica_Nohan

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ejqdE9G8WHUds4IQi7aOjQqUUSmT2SOa

# 1 - Variáveis e Tipos de Dados
"""

'''
1.1. Crie variáveis para armazenar o nome, idade, peso e altura de uma pessoa.
Imprima os valores e os tipos de dados dessas variáveis.
'''
nome = 'Nohan'
idade = 23
peso = 90
altura = 1.70
print('Nome - ',nome, 'Idade - ',idade, 'Peso - ',peso, 'Altura - ',altura)
print(f'Nome - {type(nome)} | Idade - {type(idade)} | Peso - {type(peso)} | Altura - {type(altura)}')

'''
1.2. Atualize a variável de peso para um valor diferente e imprima o novo valor.
'''
peso = 90
peso1 = 70
print(f'Peso antigo {peso}, novo peso {peso1}')

"""# 2 - Operadores Matemáticos"""

from binascii import b2a_base64
'''
2.1. Crie uma variável a com valor 10 e uma variável b com valor 3. Realize as
seguintes operações e imprima os resultados:
Soma
Subtração
Multiplicação
Divisão
Parte inteira da divisão
Resto da divisão
Exponenciação
'''
a = 10
b = 3
soma = a + b
print('Soma - ', soma)
subtracao = a - b
print('Subtração - ', subtracao)
multiplicacao = a * b
print('Multiplicação - ', multiplicacao)
divisao = a / b
print(f'Divisão - {divisao:.2f}')
inteira = a//b
print('Parte inteira da divisão - ', inteira)
resto = a%b
print('Resto - ', resto)
exponenciacao = a**b
print('Potencia - ', exponenciacao)

"""# 3 - Entrada de Dados pelo Usuário

"""

'''
3.1. Peça ao usuário para digitar seu nome e armazene em uma variável. Imprima
uma mensagem de boas-vindas usando o nome fornecido.
'''
nome = input('Digite seu nome: ')
print(f'Seja bem vindo {nome}!')

'''
3.2. Peça ao usuário para digitar sua idade, peso e altura. Calcule o IMC e
imprima o resultado arredondado para três casas decimais.
'''
idade = int(input('Por favor digite sua idade: '))
peso = float(input('Agora digite seu peso: '))
altura = float(input('Por último digite sua altura: '))
imc = peso/(altura**2)
print(f'Seu IMC é de {imc:.2f}.')

"""# 4 - Função de Impressão"""

'''
4.1. Peça ao usuário para digitar um número e imprima o número digitado.
'''
numero = int(input('Digite um número: '))
print(f'O número digitado foi {numero}.')

'''
4.2. Peça ao usuário para digitar dois números e imprima a soma deles.
'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
result = num1 + num2
print(f'A soma dos números digitados é de {result}.')

"""# 5 - Métodos de Strings"""

'''
5.1. Peça ao usuário para digitar um e-mail e verifique se o e-mail contém o
caractere '@'. Imprima uma mensagem indicando se é um e-mail válido ou não.
'''
email = input('Digite seu email: ')
valida = '@' in email
print(valida)

'''
5.2. Peça ao usuário para digitar uma frase e:
Converta a frase para maiúsculas.
Converta a frase para minúsculas.
Converta a primeira letra de cada palavra para maiúscula.
Verifique se a frase começa com uma determinada palavra (ex.: 'Olá').
'''
frase = input('Digite uma frase: ')
maiuscula = frase.upper()
muniscula = frase.lower()
inicioMaiuscula = frase.title()
verifica = 'Olá' in inicioMaiuscula
print(frase)
print(maiuscula)
print(muniscula)
print(inicioMaiuscula)
print(verifica)

"""# 6 - Listas"""

'''
6.1. Crie uma lista com os nomes de cinco amigos. Imprima o nome do terceiro
amigo na lista.
'''
amigos = ['João', 'Mario', 'Leticia', 'Ana', 'Lucas']
print(amigos[2])

'''
6.2. Adicione um novo nome à lista de amigos e remova o primeiro nome.
Imprima a lista atualizada.
'''
amigos.append('Luana')
amigos.remove('João')
print(amigos)

'''
6.3. Crie uma lista com as idades dos seus amigos e:
Imprima a idade do amigo mais velho.
Imprima a idade do amigo mais novo.
Calcule e imprima a soma das idades.
'''
idades = [23, 26, 20, 24, 22]
maior = max(idades)
menor = min(idades)
soma = sum(idades)
print(f'A maior idade é {maior}')
print(f'A menor idade é {menor}')
print(f'A soma das idades é {soma}')

"""#7 - Tuplas"""

'''
7.1 Crie uma tupla com as informações de um cliente (nome, idade, peso, altura).
Imprima todas as informações.
'''
cliente = ('João', 45, 80, 1.75)
print(type(cliente))
print(cliente)

'''
7.2. Crie uma nova tupla concatenando a tupla do exercício anterior com o e-mail
do cliente. Imprima a nova tupla.
'''
email_cliente = ('joao_joao@gmail.com',)
cliente1 = cliente + email_cliente
print(cliente1)

"""# 8 - Dicionários"""

'''
8.1. Crie um dicionário com informações de um cliente
(nome, idade, peso, altura). Imprima o valor associado à chave 'nome'.
'''
dicionario = {'nome':'João','idade':23,'peso':70,'altura':1.75}
print(dicionario['nome'])

'''
8.2. Adicione uma nova chave 'email' ao dicionário do exercício anterior e
imprima o dicionário atualizado.
'''
dicionario['email'] = 'joao_joao@gmail.com'
print(dicionario)

'''
8.3. Remova a chave 'peso' do dicionário e verifique se a chave 'endereço' está
no dicionário. Imprima os resultados.
'''
dicionario = {'nome':'João','idade':23,'peso':70,'altura':1.75}
dicionario.pop('peso')
endereco = dicionario.get('endereço')
print(dicionario)
print(endereco)

"""#9 - Controle de Fluxo"""

'''
9.1. Peça ao usuário para digitar sua idade e verifique se ele é menor de idade,
 adulto ou idoso. Imprima uma mensagem correspondente.
'''
idade = int(input('Digite sua idade para a verificação: '))
if idade < 18:
  print('Menor de idade.')
elif idade >= 18 and idade < 65:
  print('Adulto.')
else:
  print('Idoso.')

'''
9.2. Peça ao usuário para digitar uma nota (0 a 100) e imprima se ele foi
aprovado (nota >= 60) ou reprovado.
'''
nota = float(input('Digite sua nota para verificar se passou: '))
if nota >= 60:
  print('Parabens você passou!')
else:
  print('Infelizmente você não passou.')

'''
9.3. Crie uma lista com os nomes de cinco cidades. Use um loop for para imprimir
cada nome de cidade.
'''
cidades = ['São Bernardo do Campo', 'São Paulo', 'Santo André', 'São Caetano', 'Diadema']
for indice, cidade in enumerate(cidades, start=1):
  print(indice, ' - ', cidade)

'''
9.4. Crie uma lista com os números de 1 a 10. Use um loop for para imprimir o
quadrado de cada número.
'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice, x in enumerate(numeros, start=1):
  valor = x**2
  print(f'{indice} ao quadrado é {valor}')

"""#10 - Funções"""

'''
10.1. Crie uma função chamada verificar_numero que receba um número e retorne:

"Positivo" se for maior que 0.
"Negativo" se for menor que 0.
"Zero" se for igual a 0.
'''
def verificar_numero(valor):
  if valor > 0:
    print('Positivo.')
  elif valor < 0:
    print('Negativo.')
  elif valor == 0:
    print('Zero.')

numero = int(input('Digite um número inteiro qualquer: '))
verificar_numero(numero)

'''
10.2. Crie uma função chamada calcular_troco que receba o valor de uma compra e
o valor pago pelo cliente. A função deve retornar o troco.
Se o valor pago for menor que o valor da compra, a função deve retornar uma
mensagem informando que o pagamento é insuficiente.
'''
def calcular_troco(compra,recebido):
  if recebido < compra:
    print('Pagamento insuficiente, verifique e tente novamente.')
  else:
    troco = recebido - compra
    print(f'O troco sera de {troco:.2f}.')

compra = float(input('Qual o valor da compra? '))
recebido = float(input('Valro recebido pelo cliente: '))
calcular_troco(compra,recebido)

'''
10.3. Crie uma função chamada contar_palavras que receba uma frase como
argumento e retorne quantas palavras existem nela.
'''
def contar_palavras(frase):
  palavra = frase.split()
  for x in range(len(palavra)):
    x += 1
  print(f'O total de palavras é de {x}.')

frase = input('Digite uma frase: ')
contar_palavras(frase)

"""#11 - Extra (desafio opcional)"""

'''
Contexto

Gandalf decide sair em viagem à procura de um ladrão para a comitiva de Thorin,
escudo de carvalho. Analisando a situação e procurando não levar muito itens,
Gandalf então decide levar apenas 3 dos itens abaixo:

- Espada Longa
- Cajado
- Cachimbo c/ erva de fumo
- Algibeira
- Pergaminho antigo
- Uma semente misteriosa

Ajude o Gandalf a escolher os seus itens
'''

'''
Contexto:
Uma escola precisa analisar as notas de seus alunos e determinar se cada aluno
foi aprovado ou reprovado. As notas serão armazenadas em uma lista e a análise
deve ser realizada em um loop.
'''

'''
Requisitos:
Peça ao usuário para inserir o nome e a nota de cinco alunos.
Armazene os nomes e as notas em listas separadas.
Para cada aluno, verifique se a nota é maior ou igual a 60. Se sim, o aluno está
aprovado; caso contrário, está reprovado.
Exiba uma mensagem para cada aluno informando seu nome, nota e se foi aprovado
ou reprovado.
'''
alunos_sala = []
notas_sala = []
def verifica_notas(alunos,notas):
  for aluno in range(len(alunos)):
    for nota in range(len(notas)):
      if nota == aluno:
        if notas[nota] >= 60:
          print(f'O/A aluno(a) {alunos[aluno]} passou!')
        else:
          print(f'O/A aluno(a) {alunos[aluno]} reprovou.')

for x in range(5):
  aluno1 = input('Digite o nome do aluno: ')
  alunos_sala.append(aluno1)
  nota1 = int(input('Digite a nota do aluno: '))
  notas_sala.append(int(nota1))
verifica_notas(alunos_sala,notas_sala)

'''
Contexto
Uma empresa deseja realizar uma pesquisa de opinião com cinco participantes
sobre um novo produto. As respostas devem ser armazenadas e analisadas para
verificar a satisfação dos clientes.
'''

'''
Requisitos
Peça ao usuário para inserir o nome e a opinião (satisfeito/insatisfeito) de
cinco participantes.
Armazene os nomes e as opiniões em um dicionário.
Conte o número de participantes satisfeitos e insatisfeitos.
Exiba a lista de participantes satisfeitos e insatisfeitos, bem como o número
total de cada categoria.
'''
pesquisa = {}
tentativa = []
participantesSatisfeitos = []
participantesInsatisfeitos = []
def pesquisaSatisfacao (pesquisa):
  for indice, chave in enumerate(pesquisa):
    satis = pesquisa.get(chave)
    if satis == 'Satisfeito' or satis == 'Satisfeita':
      participantesSatisfeitos.append(chave)
    else:
      participantesInsatisfeitos.append(chave)

  satisfeitos = len(participantesSatisfeitos)
  insatisfeitos = len(participantesInsatisfeitos)
  print(f'Os participantes satisfeitos são {participantesSatisfeitos}, sendo um total de {satisfeitos}.')
  print(f'Os participantes insatisfeitos são {participantesInsatisfeitos}, sendo um total de {insatisfeitos}.')




for x in range(5):
  participante = input('Digite o nome do participante: ')
  participante = participante.capitalize()
  satisfacao = input('Digite a nota do participante: ')
  satisfacao = satisfacao.capitalize()
  pesquisa[participante] = satisfacao
  # print(pesquisa)
pesquisaSatisfacao(pesquisa)