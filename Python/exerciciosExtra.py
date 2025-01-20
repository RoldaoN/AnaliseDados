# Exercícios if, elif e else

'''
1-Faça um Programa que leia três números inteiros e mostre eles em ordem crescente.
'''
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# num3 = int(input('Digite o terceiro número: '))
# if num1 > num2 and num2 > num3 and num1>num3:
#     print(num1, num2, num3)
# elif num1<num2 and num2>num3 and num3<num1:
#     print(num2,num1,num3)
# elif num1<num2 and num2>num3 and num3>num1:
#     print(num2,num3,num1)
# elif num1<num3 and num3>num2 and num1<num2:
#     print(num3,num2,num1)
# else:
#     print(num3,num1,num2)


'''
2-Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
'''
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# num3 = int(input('Digite o terceiro número: '))
# if num1<num2 and num2<num3 and num1<num3:
#     # 1
#     # 2
#     # 3
#     print('maior ',num3,'menor ',num1)
# elif num1<num2 and num2>num3 and num1>num3:
#     # 2
#     # 3
#     # 1
#     print('maior ',num2,'menor ',num3)
# elif num1>num2 and num2<num3 and num3<num1:
#     # 3
#     # 1
#     # 2
#     print('maior ',num1,'menor ',num2)
# elif num1>num2 and num2>num3 and num3<num1:
#     print('maior ',num1,'menor ',num3)
#     # 3
#     # 2
#     # 1
# else:
#     # 2
#     # 3
#     # 1
#     print('maior ',num2,'menor ',num3)


'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
# dia = input('Digite M para Manhã, T para Tarde e N para Noite: ')
# if dia == 'M':
#     print('Bom dia!')
# elif dia == 'T':
#     print('Boa tarde!')
# elif dia == 'N':
#     print('Boa noite!')
# else:
#     print('Valor Inválido')


'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''
# salario = float(input('Qual seu salário? '))
# if salario <= 280.00:
#     porcent = (salario*(20/100))
#     reajuste = salario + porcent
#     print(f'Seu salário era de R${salario}, teve um aumento de 20% aumentando mais R${porcent:.2f} ficando em R${reajuste:.2f}')
# elif salario > 280.00 and salario <=700.00:
#     porcent = (salario*(15/100))
#     reajuste = salario + porcent
#     print(f'Seu salário era de R${salario}, teve um aumento de 15% aumentando mais R${porcent:.2f} ficando em R${reajuste:.2f}')
# elif salario > 700.00 and salario<=1500.00:
#     porcent = (salario*(10/100))
#     reajuste = salario + porcent
#     print(f'Seu salário era de R${salario}, teve um aumento de 10% aumentando mais R${porcent:.2f} ficando em R${reajuste:.2f}')
# else:
#     porcent = (salario*(5/100))
#     reajuste = salario + porcent
#     print(f'Seu salário era de R${salario}, teve um aumento de 5% aumentando mais R${porcent:.2f} ficando em R${reajuste:.2f}')


'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# media = (nota1+nota2)/2
# if media <= 10 and media >= 9:
#     print(f'As notas foram {nota1} e {nota2}, com uma média de {media:.2f}, ficando com o conveito A, estando APROVADO.')
# elif media >=7.5 and media < 9:
#     print(f'As notas foram {nota1} e {nota2}, com uma média de {media:.2f}, ficando com o conveito B, estando APROVADO.')
# elif media >= 6 and media < 7.5:
#     print(f'As notas foram {nota1} e {nota2}, com uma média de {media:.2f}, ficando com o conveito C, estando APROVADO.')
# elif media >= 4 and media < 6:
#     print(f'As notas foram {nota1} e {nota2}, com uma média de {media:.2f}, ficando com o conveito D, estando REPROVADO.')
# else:
#     print(f'As notas foram {nota1} e {nota2}, com uma média de {media:.2f}, ficando com o conveito E, estando REPROVADO.')


'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
# dia = int(input('Digite o dia: '))
# mes = int(input('Digite o mês: '))
# ano = int(input('Digite um ano: '))
# valida = False
# if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
#     if dia<=31:
#         valida = True
# elif mes==4 or mes==6 or mes==9 or mes==11:
#     if dia<=30:
#         valida = True
# elif mes ==2:
#     if (ano%4==0 and ano%100!=0) or (ano%400==0):
#         if dia<=29:
#             valida = True
#         elif dia<=28:
#             valida = True

# if valida:
#     print('Data valida!')
# else:
#     print('Data invalida.')


'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
# num = int(input('Digite um número inteiro: '))
# if num<1000:
#     centena = num//100
#     dezena = (num%100)//10
#     unidades = (num%100)%10
#     if centena != 0:
#         print(centena, 'centenas', dezena, 'dezenas', unidades, 'unidades.')
#     elif centena == 0 and dezena != 0:
#         print(dezena, 'dezenas', unidades, 'unidades.')
#     else:
#         print(unidades,'unidades.')
# else:
#     print('Número invalido. por favor digite outro.')


'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
# def dinheiro (valor):
#     centena = saque//100
#     dezena = (saque%100)//10
#     nota50 = dezena//5
#     unidades = (saque%100)%10
#     nota10 = dezena%5
#     nota5 = unidades//5
#     nota1 = unidades%5
#     if saque>=10 and saque<=600:
#     #print('nota 100 - ', centena, '|dezenas - ', dezena, '|notas de 50 - ', nota50, '|unidades - ', unidades, '|notas de 10', nota10, '|notas de 5', nota5, '|notas de 1', nota1)
#         if centena != 0 and nota50 != 0 and nota5 != 0 and nota1 != 0:
#             print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota50, 'notas de R$50,00, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         elif centena != 0 and nota50 == 0 and nota10 != 0:
#             print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         elif centena == 0 and nota50 != 0:
#             print('A máquina fornecerá a você ', nota50, 'notas de R$50,00, ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         else:
#             print('A máquina fornecerá a você ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#     else:
#         print('Valor de saque invalodo, por favor tente novamente.')

# saque = int(input('Qual o valor que gostaria de sacar? '))
# dinheiro(saque)

# if saque>=10 and saque<=600:
#     dinheiro
#     #print('nota 100 - ', centena, '|dezenas - ', dezena, '|notas de 50 - ', nota50, '|unidades - ', unidades, '|notas de 10', nota10, '|notas de 5', nota5, '|notas de 1', nota1)
#     if centena != 0 and nota50 != 0 and nota5 != 0 and nota1 != 0:
#         print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota50, 'notas de R$50,00, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#     elif centena != 0 and nota50 == 0 and nota10 != 0:
#         print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#     elif centena == 0 and nota50 != 0:
#         print('A máquina fornecerá a você ', nota50, 'notas de R$50,00, ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#     else:
#         print('A máquina fornecerá a você ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
# else:
#     print('Valor de saque invalodo, por favor tente novamente.')



'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
# a = 80000
# b = 200000
# ano = 0
# # a1 = 0
# # b1 = 0
# while a < b:
#     a = a + (a*(3/100))
#     b = b + (b*(1.5/100))
#     ano = ano + 1
    
# print (f'Para que a população de A se iguale ou passe de B precisa de {ano} anos, chegando a uma população de A = {a:.2f} e B = {b:.2f}')


# frutas=['banana', 'maçâ', 'morango']
# for indice, fruta in enumerate(frutas):
#     frutas[indice] = fruta.upper()
# print(frutas)

# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# for linha in matriz:
#     print('----x----')
#     for coluna in linha:
#         print(coluna)

'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''
# nome = input('Digite o seu nome: ')
# indice = len(nome)
# while indice <= 4:
#     nome = input('Digite seu nome novamente: ')
#     indice = len(nome)
# idade = int(input('Digite sua idade: '))
# while idade<0 and idade>150:
#     idade = int('Digite sua idade novamente: ')
# salario = float(input('Digite seu salário: '))
# while salario < 0:
#     salario = float('Digite seu salário novamente: ')
# genero = input('Digite seu gênero\nF para Feminino\nM para masculino\n')
# genero = genero.upper()
# while genero!='F' and genero!='M':
#     genero = input('Digite seu gênero\nF para Feminino\nM para masculino\n')
#     genero = genero.upper()
# estado = input("Digite seu estado cívil: \nS para Solteiro(a/e)\nC para Casados(a/e)\nV para Viuvo(a/e)\nD para Divorciado(a/e)\n")
# estado = estado.upper()
# while estado!="S" and estado!='C' and estado!='V' and estado!='D':
#     estado = input('Digite novamente seu estádo cívil: ')
# print('Dados validados')


'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e
ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
'''
# tabela = []
# for indice in range(1,51):
#     preco = indice * 1.99
#     tabela.append(preco)
# print(tabela)
# quantidade = float(input('Digite a quantidade de itens comprados: '))
# for indice, valor in enumerate(tabela, start=1):
#     if indice == quantidade:
#         print(f'O valor a ser pago é de {valor}')


'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''
# troco = float(0)
# itens = 0
# total = float(0)
# preco = float(input('Digite o valor do produto: '))
# total = total + preco
# itens += 1
# while preco != 0:
#     preco = float(input('Digite o valor do produto: '))
#     total = total + preco
#     itens += 1
# print(total, itens)
# dinheiro = float(input('Valor pago pelo cliente: '))
# troco = dinheiro - total
# print(f'O valor da compra foi de {total}\nQuantidade de itens comprados {itens-1}\nO cliente pagou R${dinheiro:.2f}\nRecendo troco de R${troco:.2f}')


'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''
# fator = 1
# numero = int(input('Digite um número para ser fatorado: '))
# while numero != 0:
#     fator = fator*numero
#     numero -= 1
# print(fator)


'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
# tabuada = int(input('Qual tabuada deseja? '))
# inicio = int(input('Por qual número que que ela comece? '))
# fim = int(input('Qual o número que deseja que ela acabe? '))
# for x in range(inicio, fim+1):
#     if fim > inicio:
#         mult = x*tabuada
#         print(f'{tabuada} X {x} = {mult}')


'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.
'''
# salarioInicial = float(input('Qual o salario inicial do funcionario? '))
# ano = 1995
# percentual = 1.5
# while ano != 2024:
#     porcent = salarioInicial*(1.5/100)
#     salario = salarioInicial + porcent
#     ano +=1
#     if ano < 2024 and ano > 1996:
#         aumento = salario*((1.5/100)*2)
#         salario = salario*aumento
#         ano +=1
# print(f'Com o salario inicial de {salarioInicial},hoje essa pessoa ganha {salario}')


'''
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''
# numeroAluno = [1,2,3,4,5,6,7,8,9,10]
# alturaAluno = [160,170,175,163,180,174,179,164,150,176]
# maior = max(alturaAluno)
# menor = min(alturaAluno)
# for indice, altura in enumerate(alturaAluno):
#     if altura == maior:
#         print(f'O aluno mais alto é o {numeroAluno[indice]} com altura de {maior}cm')
#     elif altura == menor:
#         print(f'O menor aluno é o {numeroAluno[indice]} com a altura de {menor}')


'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''
# divida = float(input('Digite o valor da divida'))
# for parcela in range(0,12,3):
#     for juros in range(0,25,5):
#         juros1 = divida*(juros/100)
#         parcelas = juros/parcela
#         print(f'Valor da divida - juros - parcelas valor da aprcela\n{juros1}')


# soma = []
# for x in range(1,101):
#     soma.append(int(x))
#     result = sum(soma)
# print(result)


# soma = 0
# for x in range(1,101):
#     soma = soma + x
# print(s

# from modulos.moduloTeste import revisaTexto
# texto = input('Digite o texto: ')
# palavra = input('Digite uma palavra para verifica-la no texto: ')
# numero = revisaTexto(texto,palavra)
# print(f'A palavra {palavra} aparece {numero} vezes no texto')

# from exercicios_25_11_2024 import contaPalavra
# frase = input('Digite uma frase: ')
# contaPalavra(frase)


# email = 'doug@gmail.com'
# print(len(email))


'''
Atividade 12

Crie uma função chamada converter_temperatura que receba uma
temperatura e o tipo de conversão desejada (Celsius para
Fahrenheit, Celsius para Kelvin, Fahrenheit para Celsius, etc.).
Use um parâmetro adicional para determinar a conversão.
'''
# from modulos.moduloTeste import conversaoTemp
# temp = float(input('Digite a temperatura desejada: '))
# conversaoTemp(temp)


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
