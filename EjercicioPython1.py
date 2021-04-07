def tableroVacio():
            return[
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     ]


def soltarFichaEnColumna(ficha, tablero, columna):
             for fila in range(6, 0, -1):
                     if tablero[fila-1][columna-1] == 0:
                             tablero [fila-1][columna-1]=ficha
                             return


def dibujarTablero(tablero):
             for fila in range(6):
                     print(tablero[fila])
                     print("\n")

def completarTableroEnOrden(tablero, secuencia):
     y=2
     for x in secuencia:
             if y==2:
                     y=1
                     soltarFichaEnColumna(y,tablero,x)
             else:
                     y=2
                     soltarFichaEnColumna(y,tablero,x)

secuencia = [1,2,3,1]
tablero=tableroVacio()
completarTableroEnOrden(tablero,secuencia)
dibujarTablero(tablero)




