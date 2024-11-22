'''
# 1 - Crie uma variável chamada sétima, ela deve ter o 7º caracter da string email
email = 'doug@gmail.com'
setima = email[6]
print(setima)

# 2- Uma placa de carro tem o formato "ABC-1234". Extraia apenas os números da placa usando slicing.
# Exemplo:
# Entrada: "ABC-1234"
# Saída esperada: "1234"
placa = 'ABC-1234'
print(placa[4:8])

# 3 - Verifique se o nome de um produto contém a palavra 'promoção'.
# Exemplo:
# Entrada: "Liquidificador em promoção"
# Sáida esperada: True
produto = 'Liquidificador em promoção'
result = 'promoção' in produto
print(result)

# 4 - Verifique se o número de telefone começa com o DDD "11".
# Exemplo: 11-91234-5678
tel = '11-91234-5678'
result = tel.startswith('11')
print(result)
'''

# 5 - Receba uma lista de nomes separados por vírgulas e transforme-a em uma lista python
# Exemplo: nomes = "Ana,Bruno,Carla,Daniel"
nomes = 'Ana,Bruno,Carla,Daniel'
nomes1 = nomes.split(',')
print(nomes1, type(nomes1))
#print(len(nomes1))