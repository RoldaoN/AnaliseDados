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
numero = 9
for x in range(1,11):
    mult = numero*x
    print(f'{numero} X {x} = {mult}')
