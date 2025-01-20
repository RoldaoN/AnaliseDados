def revisaTexto(texto,palavra):
    num = 0
    for p in range(len(texto)):
        if texto[p:p + len(palavra)] == palavra:
            num += 1
    return num

def conversaoTemp(valor):
    escolha = int(input('A temperatura digitada está em:\n1 - °Celcius\n2 - °Fahrenheit\n3 - °Kelvin\n'))
    transforma = int(input('Agora deseja tranformar ela em:\n1 - °Celcius\n2 - °Fahrenheit\n3 - °Kelvin\n'))
    if escolha == 1 and transforma == 2:
        cF = (valor*(9/5))+32
        print(f'A temperatura de {valor}°C é igual a {cF:.2f}°Fahrenheit.')
    elif escolha == 1 and transforma == 3:
        cK = valor + 273.15
        print(f'A temperatura de {valor}°C é igual a {cK:.2f}°Kevin.')
    elif escolha == 2 and transforma == 1:
        fC = 5/9*(valor-32)
        print(f'A temperatura de {valor}°Fahrenheit é igual a {fC:.2f}°C.')
    elif escolha == 2 and transforma == 3:
        fK = (temp - 32)*(5/9)+273.15
        print(f'A temperatura de {valor}°Fahrenheit é igual a {fK:.2f}°Kelvin.')
    elif escolha == 3 and transforma == 1:
        kC = temp - 273.15
        print(f'A temperatura de {valor}°Kelvin é igual a {kC:.2f}°C.')
    else:
        kF = (temp - 273.15)*(9/5)+32
        print(f'A temperatura de {valor}°Kelvin é igual a {kF:.2f}°C.')