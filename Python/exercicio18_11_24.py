import math
'''
'''
# 1-Crie um programa que some dois números inteiros e mostre o resultado.
num1= 10
num2= 16
result = num1+num2
print('O resultado da soma é:', result)

# 2-Crie variáveis para armazenar: um número inteiro, um número decimal, uma palavra, e um valor booleano. Imprima cada variável com seu tipo usando print.
num1 = 20
num2 = 3.14
palavra1 = 'Sorvete'
valorbool = True
print('O num1 é um', type(num1), 'O num2 é um:',type(num2),'A palavra1 é uma',type(palavra1),'o valorbool é um',type(valorbool))

# 3-Crie um programa que junte duas strings em uma só.
frase1 = "Eu estou estudando na"
frase2 = "SoulCode!"
print(frase1+' ',frase2)

# 4-Exercício sobre operadores e print
base = 20
altura = 15
result = base * altura
print ('A área do retângulo é de ', result, 'm^2')

# 5-Exercício de média e print
nota1 = 8
nota2 = 6
media = (nota1+nota2)/2
print(media)

# 7-Crie um programa que calcule quantos anos uma pessoa terá daqui a 10 anos.
idade=24
idade=idade+10
print('A pessoa terá',idade,'anos')

# 8-Crie um programa que calcule a diferença entre dois números.
num1=37
num2=92
result=num2-num1
print('A diferença entre eles é de ',result)

# 9-Multiplicação de dois números
num1=3
num2=5
result=num1*num2
print('O valor da multiplicação será', result)

# 10-Divisão de dois números
num1=30
num2=3
result=num1/num2
print('O valor da divisão será de ',result)

# 11-Crie um programa que calcule o quadrado de um número.
num1=4
result=num1**num1
print('A potência do número será: ',result)

# 12-Crie um programa que mostre o resto da divisão entre dois números.
num1=15
num2=2
result=num1%num2
print('O resto da divisão será de', result)

# 13-Calcule o resultado da seguinte expressão matemática:
result = (10+20)*2-15/3
print('O resultado da opeção "(10+20)*2−15/3" é de ', result)

# 14-Exercício de minutos para segundos
minutos = 7
segundos = minutos*60
print(minutos, 'minutos tem', segundos)

# 15-Calcule o valor final de um produto que custa R$100, com um desconto de 20%.
preco=100
desconto=preco*(20/100)
preco -= desconto
print('O produto com o desconto de 20% ficará em: ', preco)

# 16-Crie um programa que divida dois números inteiros e mostre apenas o resultado inteiro da divisão.
num1 = 17
num2 = 3
result = num1//num2
print('O resultado inteiro da divisão será de ',result)

# 17-Converta uma quantidade de horas em segundos.
horas=3
segundos=(horas*60)*60
print(horas,"serão",segundos,'segundos')

# 18-Calcule o perímetro de um círculo, sabendo que a fórmula é:
raio=12
perimetro=2*math.pi*raio
print(f'O perímetro da circunferência será de {perimetro:_.2f}')

# 19-Calcule o preço total de 5 itens que custam R$25 cada.
preco=25
result=preco*5
print('O preço dos 5 produtos juntos será de R$',result)

# 20-Conversão de Temperatura
temp= 53
celsius = 5/9*(temp-32)
print('A temperatura de',temp,f'Fahrenheit será {celsius:_.2f} em Celsius')

# 21-Calcule o IMC
print('Vamos calcular seu IMC.')
peso=float(input('informe seu peso'))
altura=float(input('Agora informe sua altura'))
imc=peso/(altura**2)
print('seu IMC é de ',imc)

# 22-Peça o ano de nascimento do usuário e calcule sua idade aproximada
ano=int(input('Em que ano você nasceu? '))
idade=2024-ano
print('Você tem ',idade,'anos')

#23- Peça o preço de um produto e a porcentagem de desconto, mostre o preço final
preco=float(input('Informe o preço do protudo: '))
desconto=float(input('Qual o desconto do produto? '))
desconto=preco*(desconto/100)
preco -= desconto
print(f'O valor do produto com desconto será de R${preco:.2f}')

# 24-Peça um numero e mostre o quadrado e o cubo dele
num=float(input('Digite um número: '))
quad=num**2
cub=num**3
print('O número',num,'elevado ao quadrado resulta em',quad,'e ele elevado ao cubo fica',cub)