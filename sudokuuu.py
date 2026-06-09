def imprimir(tablero):
    for fila in tablero:
        print(fila)
    print()


def buscar_vacio(tablero):
    for f in range(9):
        for c in range(9):
            if tablero[f][c] == 0:
                return f, c
    return None


def validar(tablero, num, fila, columna):

    # Revisar fila
    for c in range(9):
        if tablero[fila][c] == num:
            return False

    # Revisar columna
    for f in range(9):
        if tablero[f][columna] == num:
            return False

    # Revisar subcuadro 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (columna // 3) * 3

    for f in range(inicio_fila, inicio_fila + 3):
        for c in range(inicio_col, inicio_col + 3):
            if tablero[f][c] == num:
                return False

    return True


def sudoku_bt(tablero):

    posicion = buscar_vacio(tablero)

    # Caso base: ya no hay espacios vacíos
    if posicion is None:
        return True

    fila, columna = posicion

    # Intentar números del 1 al 9
    for num in range(1, 10):

        if validar(tablero, num, fila, columna):

            tablero[fila][columna] = num

            # Mostrar cada avance (como en el laberinto)
            imprimir(tablero)

            if sudoku_bt(tablero):
                return True

            # Backtracking
            tablero[fila][columna] = 0

    return False


sudoku = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]

print("Sudoku inicial:")
imprimir(sudoku)

if sudoku_bt(sudoku):
    print("Sudoku resuelto:")
    imprimir(sudoku)
else:
    print("No tiene solución")