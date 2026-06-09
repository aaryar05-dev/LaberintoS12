def imprimir(mat):
    for fila in mat:
        print(fila)
    print()

def validar(lab, res, f, c):
    filas = len(lab)
    columnas = len(lab[0])

    if f < 0 or f >= filas:
        return False
    if c < 0 or c >= columnas:
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False

    return True

def laberinto(lab, res, f, c, salida):
    if not validar(lab, res, f, c):
        return False

    res[f][c] = 1
    imprimir(res)   

    if (f, c) == salida:
        return True

    if laberinto(lab, res, f + 1, c, salida):  
        return True

    if laberinto(lab, res, f, c + 1, salida):  
        return True

    if laberinto(lab, res, f - 1, c, salida):  
        return True

    if laberinto(lab, res, f, c - 1, salida): 
        return True

    res[f][c] = 0
    imprimir(res)   
    return False


lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1]
]

res = [[0 for _ in range(len(lab[0]))] for _ in range(len(lab))]

inicio = (0, 0)
salida = (8, 8)

if laberinto(lab, res, inicio[0], inicio[1], salida):
    print("salida")
else:
    print("no hay salida")