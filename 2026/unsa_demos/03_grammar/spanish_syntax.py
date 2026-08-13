def clasificar(valor):
    si valor > 0:
        retornar "positivo"
    sinosi valor == 0:
        retornar "cero"
    retornar "negativo"


for valor in (-1, 0, 1):
    print(valor, clasificar(valor))
