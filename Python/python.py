#Aprendendo Python

'''
# 1-Printar algo
print('hello world!') 

# 2-Usando conta matemática
result=6+2
print(result) 

# 3-Criando variáveis
nome = 'Nohan'
idade=26
altura = 1.67
estuda = True

tipoNome=type(nome)
print(tipoNome)

# 4-Operadores de Comparação
# 4.1-Igualdade
resul1 = 5==5
print ('são Iguais? ',resul1)
resul2 = 5==3
print ('são Iguais? ',resul2)

# 4.2-diferencial
resul1 = 5 != 3
print('são diferentes? ',resul1)
resul2 = 5 != 5
print('são diferentes? ', resul2)

# 4.3-Maior que
resul1 = 5 > 3
print('é maior que? ',resul1)
resul2 = 5 > 5
print('é maior que? ',resul2)

# 4.4-Menor que
resul1 = 3 < 5
print('é menor que? ',resul1)
resul2 = 5 < 3
print('é menor que? ',resul2)

# 4.5-Maior Igual
resul1 = 5 >= 3
print('é maior ou igual que? ',resul1)
resul2 = 5 >= 7
print('é maior ou igual que? ',resul2)

# 4.6-Menor Igual
resul1 = 3 <= 5
print('é menor ou igual que? ',resul1)
resul2 =  5<= 3
print('é menor ou igual que? ',resul2)

# 5-Operadores Lógicos
# 5.1-And - Ele só retornará verdadeiro se as duas informações forem iguais
inf1=True
inf2=True
result=inf1 and inf2
print('Com o "and", sendo as duas informações verdadeiras o resultado será',result)

# 5.6-Or - Ele só retornará falso se as duas informações forem falsas
inf1=False
inf2=False
inf3=True
result= inf1 or inf2
result1 = inf1 or inf3
print('Quando colocamos duas informações falsas ele retorna',result,'mas quando colocamos uma informação verdadeira e uma falsa temos o retorno',result1)

# 6-Input
nome=input("informe seu nome: ")
print(nome,type(nome))
# Quando usamos o input o tipo do resultado sempre será string, para mudar isso temos que tipar ele com o que queremos que ele seja
idade=int(input('Digite sua idade: '))
print(idade,type(idade))

# 7-F-Strings
# As F-Strings são a forma mais moderna e recomendada de formatar strings. Basta colocar um 'f' antes da string e incluir as variáveis entre chaves {}
preco=float(input('Informe o preço do protudo: '))
desconto=float(input('Qual o desconto do produto? '))
desconto=preco*(desconto/100)
preco -= desconto
print(f'O valor do produto com desconto será de R${preco:.2f}')

# 9-Métodos de String
# 9.1-Fatiamento de string (slicing)
# 0  1  2  3  4  5  6  7  8   9  10  11   12  13    (Indice - como o Python pensa)
# 1º 2º 3º 4º 5º 6º 7º 8º 9º 10º 11º 12º 13º 14º    (Ordinal - como nós pensamos)
# d  o  u  g  @  g  m  a  i  l    .  c    o   m
#email='doug@gmail.com'
#print(email[4])
# Imagine que você deseja criar uma variável que armazene todos os caracteres após o @ da string do email.
# No fatiamento de um intervalo o que vem antes dos : marca o índice de início do 
# fatiamento e é inclusivo. Já o que vem depois dos : marca o índice final do 
# intervalo e é exclusivo, ou seja, vai pegar até um antes do número informado.
#print(email[:])

# 9.1 - in e not in
# Verifica se tem ou não um caracter ou conjunto de caracteres especificos na string.
email = 'doug@gmail.com'
result = 'x' in email
print(result)
result = '@' in email
print(result)
result = 'D' in email
print(result)
result = 'd' not in email
print(result)

# 9.2 - Capitalize
#É um método que quando utilizado deixa apenas a primeira letra de uma string em caixa alta (maiuscula).
nome = 'nohan'
print(nome)
nome2 = nome.capitalize()
print(nome2)

# 9.3 - Title
nomeCompleto = 'nohan esteves roldão'
print(nomeCompleto)
nomeCompleto2 = nomeCompleto.title()
print(nomeCompleto2)

# 9.4 - Upper
# Coloca tudo em caixa alta.
uf = 'ba'
print(uf)
uf1 = uf.upper()
print(uf1)

# 9.5 - Lower
# Deixa tudo em minusculo.
cidade = 'SÃO PAULO'
print(cidade)
cidade1 = cidade.lower()
print(cidade1)

# 9.6 - Startswith
# Checa se uma string começa com algum caracter ou conjunto de caracteres.
email = 'doug@gmail.com'
result = email.startswith('casa')
print(result)
result = email.startswith('d')
print(result)

# 9.7 - Endswith
# Checa se uma string termina com algum caracter ou conjunto de caracteres.
email = 'doug@gmail.com'
result = email.endswith('x')
print(result)
result = email.endswith('.com')
print(result)

# 9.8 - Split
# Neste bloco vamos transformar a string única nomeCompleto em outra que armazena quantas substrings houver nessa string de acordo com um separador
nomeCompleto = 'Nohan Esteves Roldão'
print(nomeCompleto)
outra = nomeCompleto.split()
print(outra)

nomeCompleto = 'Nohan,Esteves,Roldão'
print(nomeCompleto)
outra = nomeCompleto.split(',')
print(outra)

nomeCompleto = 'Nohan, Esteves, Roldão'
print(nomeCompleto)
outra = nomeCompleto.split(', ')
print(outra)

# 10 - Len
email = 'doug@gmail.com'
print(len(email))

# 11
# 11.1 - Lista
# Estrutura da lista:
# nomeLista = [item1, item2, item3, ...]
nomes = ['Nohan','Eliane', 'Victor', 'Akira']
idade = [23, 51, 20, 25]
peso = [90, 90, 60, 80]
altura = [1.67, 1.60, 1.75, 1.70]
print(nomes[0], type(nomes[0]))
print(altura[0], type(altura[0]))

# 11.2 - Append
# O método append insere o item na última posição
nomes = ['Nohan','Eliane', 'Victor', 'Akira']
idade = [23, 51, 20, 25]
peso = [90, 90, 60, 80]
altura = [1.67, 1.60, 1.75, 1.70]
#print(nomes)
nomes.append('José')
#print(nomes)
altura.append(1.70)
#print(altura)

# 11.2 - Insert
# Inserir algo na lista entre duas posições da lista
nomes = ['Nohan','Eliane', 'Victor', 'Akira']
nomes.insert(3,'jose')
#print(nomes)

# 11.3 - Substituição
# Podemos subtituir algo na lista
nomes[3] = 'Daniel'
print(nomes)

# 11.4 - Pop
# Deleta lago na lista
# nomes.pop(3)
# print(nomes)

# 11.5 - Remove
# Podemos remover também o usando o remove
nomes.remove('Daniel')
#print(nomes)

# 11.6 - Del
# Outra forma de deletar é usando o Del e passando o número do indice a ser removido
# del nomes[3]
# print(nomes)

# 11.7 - Index
# Usado para descobrir o indice de um dado da lista, mas não sabemos sua posição na mesma
nomes = ['Nohan','Eliane', 'Victor', 'Akira']
indice = nomes.index('Akira')
print(indice)

# 11.8 - Count
# Com o count podemos verificar quantas vezes um item aparece na lista
nomes = ['Nathan', 'Matheus', 'Emily', 'Francisca', 'Jean', 'Josa']
registro = nomes.count('Jean')
print(registro)

# 11.9 - Sort
# Com ele podemos colocar os itens em ordem crescente
nomes.sort()
print(nomes)

# 11.10 - Reverse
# Da mesma forma, podemos usar o reverse para colocar os itens em ordem decrescente
nomes.reverse()
print(nomes)

# 11.11 - Max
# Com o max podemos saber qual o maior valor na lista
nomes = ['Nathan','Matheus','Emily','Francisca','Jean','Josa']
idades = [26, 21, 26, 46, 48, 56]
pesos = [75, 82, 65, 63, 80, 61]
alturas = [1.73, 1.80, 1.65, 1.60, 1.73, 1.64]

maxAltura = max(alturas)
print(maxAltura)

# 11.12 - Min
# Com o nim podemos saber qual o valor minimo da lista
minAltura = min(alturas)
print(minAltura)

# 11.13 - Sum
# Com ele podemos somar todos os itens da lista
result = sum(idades)
print(result)

# 11.14 - Clear
# Usamos para limpar a lista
compras = ['banana','laranja','limão']
print(compras)
compras.clear()
print(compras)

# 12 - Tupla
'''
# Em python as tuplas são imutáveis.
# Podem ser declaradas de duas maneiras:
# nome_tupla = (item1, item2, item3...)
# nome_tupla = item1, item2, item3...

# Listas são declaradas entre []
# Tuplas são declaradas entre()
'''
nomes = ['Nathan','Matheus','Emily','Francisca','Jean','Josa']
nomes2 = ('Nathan','Matheus','Emily','Francisca')
print(nomes)
print(nomes2)

# 12.1 - Transformando uma lista em tupla
nomes = ['Nathan','Matheus','Emily','Francisca','Jean','Josa']
print(nomes)
print(type(nomes))
nomes = tuple(nomes) #Convertendo uma lista para tupla
print(nomes)
print(type(nomes))

# 12.2 - Concatenando tuplas
tupla1 = (1,2,3)
tupla2 = (4,50,6)
tupla3 = (7,8,9)

tupla_final = tupla1 + tupla2 + tupla3
print(tupla_final)

# 12.3 - Convertendo tupla para lista
nomes2 = ('Nathan','Matheus','Emily','Francisca')
print(nomes2)
print(type(nomes2))
nomes2 = list(nomes2) #Conversão para lista
print(nomes2)
print(type(nomes2))

# 12.4 - Os tópicos que usamos na lista, podemos usar na tupla também  como o count, len, index, mas, min, sum

# 13 - Dicionários
'''
# Um dicionário é uma estrutura de dados que não é indexada e ela tem a seguinte
# forma:
# nome_dicionario = {'chave':'valor', 'chave2':'valor2'...}

# Chave : Valor
'''
carro = {'marca':'vw','modelo':'gol','cor':'cinza','ano':2014}
print(carro)

# 13.1 - Get
# Forma segura de se recuperar o valor de um dicionário pois caso a chave não exista, ele não retornará nada
cor = carro.get('cor')
#print(cor)

# 13.2 - []
'''
# Você usa colchetes[] para acessar valores de um dicionário pq é a
# sintaxe padrão e direta para acessar valores usando uma chave
# especifica.

# Caso a chave não exista, ele retorna um erro.
'''
cor = carro['cor']
#print(cor)

# 13.3 - Keys
# Verificar as chaves do carro
chave = carro.keys()
#print(chave)

# 13.4 - ()
# Verificar os valores relacionados as chaves do dicionário
valores = carro.values()
#print(valores)

# 13.5 - Items
# Verificar chave/valor do dicionário
itens = carro.items()
print(itens)

# 13.6 - Podemos criar um dicionário com uma chave com vários valores dentro
carro = {
    'marca':'vw',
    'modelos': ['Gol', 'Polo', 'EcoSport'],
    'cor':'preto'
}
print(carro['modelos'][0])

# 13.7 - Pop
# Podemos usar o pop para tirar um itém do dicionário
carro.pop('marca')
print(carro)

# 13.8 - Popitem
# Usado para remover o ultimo item do dicionário
carro.popitem()
print(carro)

# 13.9 - Update
# Usado para adicionar algo no dicionário
carro.update({'modelo':'celta'})
print(carro)

# 13.10 - Podemos usar algumas coisas usadas na lista também como o len, del, clean

# 13.11 - Copy
# Podemos usar para copiar um dicionário para uma outra variável
carro = {'marca':'vw','modelo':'gol','cor':'cinza','ano':2014}
copia = carro.copy()
print(copia)
print(carro)

# 13.12 - Modificação
# Podemos modificar um item de do dicionário
carro = {'marca':'vw','modelo':'gol','cor':'cinza','ano':2014}
print(carro)

#Editando o valor
carro["modelo"] = 'celta'
print(carro)

# 13.13 - Criar um novo par de chave/valor
carro["placa"] = 'ABC-1234'
print(carro)
'''

# 14 - Sets
'''
# Os sets são estruturas de dados não indexadas e não ordenaveis, porém,
# são mutáveis e por meio de métodos e funções podemos realizar operações
# com eles.

# lista = [item1, item2, item3...]
# tupla = (item1, item2, item3...)
# dicionario = {chave:valor, chave:valor, chave:valor...}
# nome_conjunto = {item1, item2, item3}
biscoito = {'Matheus','Yasmin','Emily'}
bolacha = {'Matheus','Emily','Pietro'}
print(biscoito)
print(bolacha)

# 14.1 - Add
# Usamos para adicionar algum valor
biscoito.add('Nathan')
print(biscoito)
bolacha.add('Nathan')
print(bolacha)

# 14.2 - Remove
# Remove algo do set
biscoito.remove('Nathan')
print(biscoito)

# 14.3 - Discard
# Usado para remover um elemento específico do conjunto(set), sem gerar erro se não existir
biscoito.discard('Nathan')
print(biscoito)

# 14.4 - Union
# Unindo dois sets sem repetir um item que tem igual nos sets
biscoito = {'Matheus', 'Yasmin', 'Emily'}
bolacha = {'Matheus', 'Emily', 'Pietro'}
galera_toda = biscoito.union(bolacha)
# print(biscoito)
# print(bolacha)
# print(galera_toda)

# 14.5 - Intersection
# Usdado para descobrir quem está nos dois sets
panelinha = biscoito.intersection(bolacha)
# print(bolacha)
# print(biscoito)
# print(panelinha)

# 14.5 - Difference
# Usado para ver quem está em um único set
time_biscoito = biscoito.difference(bolacha)
time_bolacha = bolacha.difference(biscoito)
# print(bolacha)
# print(biscoito)
# print(time_biscoito)
# print(time_bolacha)

# 14.6 - Update
# Usado para colocar os itens de um ste em outro
bolacha.update(biscoito)
print(bolacha)

# 15 - Estruturas Condicionais
# 15.1 - If
'''
# Imagine que você deseja receber do usuário uma nota de 0 a 10
# e caso a nota seja maior ou igual a 6, exiba a mensagem aprovado,
# caso contrário exiba a mensagem reprovado.
'''
# nota = float(input('Informe uma nota de 0 a 10: '))
# if nota >= 6:
#   print('Aprovado')
# else:
#   print ('reprovado')


nota = float(input('Informe uma nota de 0 a 10: '))
if nota >= 6:
  print('Aprovado')
elif nota >= 4:
  print('Recuperação!')
else:
  print('reprovado')
'''

