def clasificar(valor):
    if valor > 0:
        return "positivo"
    elif valor == 0:
        return "cero"
    return "negativo"


for valor in (-1, 0, 1):
    print(valor, clasificar(valor))
