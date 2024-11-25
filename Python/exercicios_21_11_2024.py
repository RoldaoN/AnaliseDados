'''
1. Verificação de idade para habilitação

Escreva um programa que pergunte a idade de uma pessoa e informe se
ela pode ou não tirar carteira de motorista (idade mínima: 18 anos).
'''
idade = int(input('Informe sua idade: '))
if idade >= 18:
    print('Você já pode tirar a carteira de motorista!')
else:
    print('Você ainda não pode tirar a carteira de motorista.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
2. Verificar se uma loja dá desconto

Pergunte o valor total da compra e verifique se ela é maior que
R$100. Se for, aplique 10% de desconto e mostre o valor final.
Caso contrário, informe que não há desconto.
'''
preco = float(input('Entre com o valor da compra: '))
if preco >= 100:
    desconto = preco*(10/100)
    precoFinal = preco - desconto
    print('Sua compra foi no valor de R$',preco,f', com isso ganhou um desconto de 10% ficando no total de R${precoFinal:.2f}.')
else:
    print('Sua compra foi no total de R$',preco,'não obtendo desconto.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
3. Descobrir se um número é par ou ímpar

Pergunte um número ao usuário e informe se ele é par ou ímpar.
'''

num = int(input('Digite um número: '))
num1 = num%2

if num1 == 0:
    print('O número ',num,' é par.')
else:
    print('O número ',num,' é impar.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
4. Verificar categoria de um atleta

Pergunte a idade de um atleta e classifique-o nas categorias: Infantil
(até 12 anos), Juvenil (13 a 17 anos) ou Adulto (18 anos ou mais).
'''

idade = int(input('Digite sua idade para verificar sua classificação: '))
if idade <=12:
    print('Sua idade é de ',idade,' portanto sua classificação é Infantil')
elif idade >=13 and idade<= 17:
    print('Sua idade é de ',idade,' portanto sua classificação é Juvenil')
else:
    print('Sua idade é de ',idade,' portanto sua classificação é Adulto')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
5. Classificação de temperatura

Pergunte a temperatura em graus Celsius e classifique:

Menor que 15°C: Frio
Entre 15°C e 25°C: Agradável
Maior que 25°C: Quente
'''

temp = float(input('Qual a temperatura atual? '))
cels = int(input('A temperatura está em Celsius? Digite 1 para sim ou 2 para não '))
if cels == 1:
    if temp <=15:
        print('A temperatura ',temp,'° indica que está frio.')
    elif temp >= 15 and temp <=25:
        print('A temperatura de ',temp,'° indica que o clima está agradével.')
    else:
        print('A temperatura de ',temp,'° indica que está calor.')
else:
    print('Por favor indique a temperatura em Celsius.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
6. Calcular preço do transporte

Pergunte a distância da viagem e calcule o preço do transporte:

Até 100 km: R$0,50 por km.
Acima de 100 km: R$0,35 por km.
'''
dist = float(input('Qual a distância em kilometros que será percorrida? '))
if dist <= 100:
    preco = dist*0.5
    print(f'com a distância de {dist:.2f} o preço dela será de {preco:.2f}')
else:
    preco = dist*0.35
    print(f'com a distância de {dist:.2f} o preço dela será de {preco:.2f}')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
7 - Validação de horário de funcionamento

Escreva um programa que pergunte a hora atual (em formato 24h) e informe se um estabelecimento está aberto.

Horário de funcionamento: das 8h às 18h.
'''
hora = int(input('Qual o horário atual? '))
if hora <= 8 or hora>=18:
    print('A loja está fechada no momento.')
else:
    print('A loja está aberta para que faça suas compras!')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
8 - Determinar o tipo de triângulo

Peça ao usuário para digitar os comprimentos de três lados e
determine se eles formam um triângulo equilátero, isósceles ou escaleno.
'''
tamanho1 = float(input('Entre com o valor do primeiro lado do triangulo: '))
tamanho2 = float(input('Entre com o valor do segundo lado do triangulo: '))
tamanho3 = float(input('Entre com o valor do ultimo lado do triangulo: '))
if tamanho1 == tamanho2 and tamanho1 == tamanho3:
    print('O triangulo com os lados medindo respectivamente ', tamanho1,' ', tamanho2,' e ', tamanho3,', sento todas as medidas iguais, isso torna ele um Triângulo Equilátero')
elif tamanho1!=tamanho2 and tamanho2==tamanho3 and tamanho1!=tamanho3:
    print('O triangulo com os lados medindo respectivamente ', tamanho1,' ', tamanho2,' e ', tamanho3,', sento todas as medidas iguais, isso torna ele um Triângulo Isóceles')
else:
    print('O triangulo com os lados medindo respectivamente ', tamanho1,' ', tamanho2,' e ', tamanho3,', sento todas as medidas iguais, isso torna ele um Triângulo Escaleno')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
9 - Verificar dias de multa na devolução de um livro

Pergunte ao usuário a data de devolução e a data prevista (em dias) e informe:

Se devolvido antes ou na data: "Devolução sem multa".
Se devolvido após a data, calcule a multa de R$2,00 por dia de atraso.
'''
devolucao = int(input('Qual a data da devolução? '))
previsto = int(input('Qual o dia marcado para devolução? '))
if devolucao<=previsto:
    print('Sua devolução foi antes do praso, não deverá pagar multa.')
else:
    multa = (devolucao-previsto)*2.00
    print('A devolução do livro está atrasada, deverá pagar uma multa de R$',multa)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
10 - Avaliação de desempenho escolar

Peça três notas de um aluno e calcule a média. Depois, informe:

Média >= 7: "Aprovado".
Média entre 5 e 7: "Recuperação".
Média < 5: "Reprovado".
'''
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
nota3 = float(input('Qual a terceira nota? '))
media = (nota1+nota2+nota3)/3
if media>=7:
    print("Está aprovado!")
elif media >= 5 and media <= 7:
    print('Está de recuperação.')
else:
    print('Está reprovado.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
11 - Cálculo de taxa de estacionamento

Pergunte o tempo de permanência (em horas) e calcule a taxa:

Até 2 horas: R$5,00 fixo.
De 3 a 6 horas: R$8,00 fixo.
Acima de 6 horas: R$12,00.
'''
tempo = float(input('Qual o tempo de permanência do veiculo? '))
if tempo <= 2:
    print('Deverá ser pago R$5,00.')
elif tempo >= 3 and tempo <= 6:
    print('Deverá ser pago R$8,00.')
else:
    print('Deverá ser pago R$12,00')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
12 - Pergunte o consumo em kWh e calcule o valor da conta:

Até 100 kWh: R$0,50 por kWh.
De 101 a 200 kWh: R$0,70 por kWh.
Acima de 200 kWh: R$1,00 por kWh.
'''
kwh = float(input('Qual o consumo de KWH? '))
if kwh <=100:
    pagar = kwh*0.5
    print(f'De acordo com seu consumo deverá ser pago o valor de R$ {pagar:.2f}')
elif kwh > 100 and kwh <= 200:
    pagar = kwh*0.7
    print(f'De acordo com seu consumo deverá ser pago o valor de R$ {pagar:.2f}')
else:
    pagar = kwh*1.00
    print(f'De acordo com seu consumo deverá ser pago o valor de R$ {pagar:.2f}')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
13 - Verificação de maioridade

Pergunte a idade de uma pessoa e informe se ela é menor de idade, maior de idade ou idosa.

Menor de 18 anos: "Menor de idade".
Entre 18 e 59 anos: "Maior de idade".
A partir de 60 anos: "Idoso".
'''
idade = int(input(' Qual a sua idade? '))
if idade <18:
    print('Menor de idade.')
elif idade >= 18 and idade <60:
    print('Maior de idade.')
else:
    print('Idoso.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
14 - Avaliação de estoque

Peça ao usuário o número de unidades de um produto no estoque e informe:

Estoque menor que 10: "Reposição urgente necessária".
Estoque entre 10 e 20: "Estoque baixo, considere repor".
Estoque maior que 20: "Estoque suficiente".
'''
produtos = int(input('Quantos produtos tem no estoque? '))
if produtos < 10:
    print('Necessaria reposição URGENTE!')
elif produtos >= 10 and produtos <20:
    print('Estoque baixo, considere reposição.')
else:
    print('Estoque suficiente.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
15 - Verificação de elegibilidade para doação de sangue

Pergunte a idade de uma pessoa e informe se ela pode doar sangue.

Idade entre 18 e 69 anos: "Apto para doar sangue".
Fora dessa faixa: "Não apto para doar sangue".
'''
idade = int(input(' Qual a sua idade? '))
if idade >= 18 and idade <70:
    print('Apto a doação de sangue!')
else:
    print('Não está apto a doação de sangue.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
16 - Verificação de faixa de velocidade

Pergunte a velocidade de um veículo e informe:

Até 40 km/h: "Velocidade segura".
Entre 41 e 80 km/h: "Velocidade moderada".
Acima de 80 km/h: "Velocidade perigosa".
'''
velocidade = int(input('Qual a velocidade atual? '))
if velocidade <=40:
    print('Está em uma velocidade segura!')
elif velocidade > 40 and velocidade <= 80:
    print('Está em uma velocidade moderada.')
else:
    print('Está em uma velocidade perigosa!')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
17. Cálculo do imposto de renda

Pergunte o salário de uma pessoa e calcule o imposto de renda:

Até R$2.112,00: Isento
De R$2.112,01 a R$2.826,65: 7,5% (menos parcela de dedução de R$158,40)
De R$2.826,66 a R$3.751,05: 15% (menos parcela de dedução de R$370,40)
De R$3.751,06 a R$4.664,68: 22,5% (menos parcela de dedução de R$651,73)
Acima de R$4.664,68: 27,5% (menos parcela de dedução de R$884,96)
'''
salario = float(input('Informe seu salário: '))
if salario <= 2112.00:
    print('Está isento do Imposto de Renda.')
elif salario > 2112.00 and salario <= 2826.65:
    pagar = ((salario*(7.5/100))-158.40)*12
    print(f'Seu Imposto de Renda anual, já descontado é de R${pagar:.2f}')
elif salario > 2826.65 and salario <= 3751.05:
    pagar = ((salario*(15/100))-370.40)*12
    print(f'Seu Imposto de Renda anual, já descontado é de R${pagar:.2f}')
elif salario > 3751.05 and salario <= 4664.68:
    pagar = ((salario*(22.5/100))-651.73)*12
    print(f'Seu Imposto de Renda anual, já descontado é de R${pagar:.2f}')
else:
    pagar = ((salario*(27.5/100))-884.96)*12
    print(f'Seu Imposto de Renda anual, já descontado é de R${pagar:.2f}')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
18 - Cálculo da mensalidade de academia

Uma academia tem planos baseados na faixa etária e no horário de treino:

Idade até 18 anos:
  Horário comum (6h às 18h): R$50/mês.
  Horário estendido (18h às 22h): R$60/mês.
Idade entre 19 e 59 anos:
  Horário comum: R$80/mês.
  Horário estendido: R$100/mês.
Idade acima de 60 anos:
  Horário comum: R$40/mês.
  Horário estendido: R$50/mês.
'''
idade = float(input('Qual sua idade? '))
horario = float(input('Qual o horário que deseja treinar? '))
if idade <=18:
    if horario >=6 and horario < 18:
        print('De acordo com sua idade e horário escolhido pagará R$50,00 de mensalidade.')
    else:
        print('De acordo com sua idade e horário escolhido pagará R$60,00 de mensalidade.')
elif idade > 18 and idade <= 59:
    if horario >=6 and horario < 18:
        print('De acordo com sua idade e horário escolhido pagará R$80,00 de mensalidade.')
    else:
        print('De acordo com sua idade e horário escolhido pagará R$100,00 de mensalidade.')
else:
    if horario >=6 and horario < 18:
        print('De acordo com sua idade e horário escolhido pagará R$40,00 de mensalidade.')
    else:
        print('De acordo com sua idade e horário escolhido pagará R$50,00 de mensalidade.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
19 - Sistema de notas escolares com bônus por frequência

Um sistema deve calcular a média final de um aluno e incluir um bônus por frequência:

Pergunte 3 notas do aluno e sua frequência (%).
Regras:
  Média >= 7.0 e frequência >= 75%: "Aprovado".
  Média >= 5.0 e frequência >= 75%: "Recuperação".
  Média < 5.0 ou frequência < 75%: "Reprovado".
  Se a frequência for maior que 90%, adicione +0.5 na média final.
'''
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
nota3 = float(input('Qual a terceira nota? '))
frequencia = float(input('Qual a frequencia desse aluno? '))
media = (nota1+nota2+nota3)/3
if media >= 7 and frequencia >= 75:
    if frequencia < 90:
        print('Aprovado')
    else:
        media = media + 0.5
        print(f'A nota desse aluno foi de {media:.2f}, pois sua frequencia aumentou a nota.')
elif media >= 5 and frequencia >= 75:
    if frequencia < 90:
        print('Recuperação')
    else:
        media = media + 0.5
        print(f'A nota desse aluno foi de {media:.2f}, pois sua frequencia aumentou a nota.')
else:
    if frequencia < 90:
        print('Recuperação')
    else:
        media = media + 0.5
        print(f'A nota desse aluno foi de {media:.2f}, pois sua frequencia aumentou a nota.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
20 - Cálculo de tarifa de transporte público com base em idade e horário

 Um sistema de transporte público calcula tarifas com base na idade e no horário de uso:

Idade até 5 anos ou acima de 65: "Gratuito".

Idade entre 6 e 17:
  Horário de pico (7h-9h ou 17h-19h): R$2,50.
  Fora do horário de pico: R$1,50.

Idade entre 18 e 64:
  Horário de pico: R$5,00.
  Fora do horário de pico: R$3,00.

Pergunte a idade e o horário para calcular a tarifa.
'''
idade = int(input('Digite sua idade: '))
if idade <= 5 or idade >= 65:
    print(' Gratuito!')
elif idade >= 6 and idade <= 17:
    horario = int(input('Qual horário deseja usar o transporte? '))
    if (7 >= horario and horario<=9) or (17 <= horario <=19):
        print('O valor da passagem será de R$2,50.')
    else:
        print('O valor da passagem será de R$1,50.')
elif idade >=18 and idade <= 65:
    horario = int(input('Qual horário deseja usar o transporte? '))
    if (7 >= horario and horario<=9) or (17 <= horario <=19):
        print('O valor da passagem será de R$5,00.')
    else:
        print('O valor da passagem será de R$3,00.')