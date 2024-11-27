def revisaTexto(texto,palavra):
    num = 0
    for p in range(len(texto)):
        if texto[p:p + len(palavra)] == palavra:
            num += 1
    return num