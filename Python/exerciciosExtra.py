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
# def dinheiro ():
#     saque = int(input('Qual o valor que gostaria de sacar? '))
#     centena = saque//100
#     dezena = (saque%100)//10
#     nota50 = dezena//5
#     unidades = (saque%100)%10
#     nota10 = dezena%5
#     nota5 = unidades//5
#     nota1 = unidades%5
#     if saque>=10 and saque<=600:
#         dinheiro
#     #print('nota 100 - ', centena, '|dezenas - ', dezena, '|notas de 50 - ', nota50, '|unidades - ', unidades, '|notas de 10', nota10, '|notas de 5', nota5, '|notas de 1', nota1)
#         if centena != 0 and nota50 != 0 and nota5 != 0 and nota1 != 0:
#             notas = print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota50, 'notas de R$50,00, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         elif centena != 0 and nota50 == 0 and nota10 != 0:
#             notas = print('A máquina fornecerá a você ',centena, 'notas de R$ 100, ', nota10, 'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         elif centena == 0 and nota50 != 0:
#             notas = print('A máquina fornecerá a você ', nota50, 'notas de R$50,00, ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#         else:
#             notas = print('A máquina fornecerá a você ',nota10,'notas de R$10,00', nota5, 'notas de R$5,00 e ', nota1, 'notas de R$1,00')
#     else:
#         notas = print('Valor de saque invalodo, por favor tente novamente.')
#     return notas

# print(dinheiro())

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

