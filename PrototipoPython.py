def tableroVacio():
            return[
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]                   
                   ]


def soltarFichaEnColumna(ficha, tablero, columna):
             for fila in range(7, 0, -1):
                     if tablero[fila-1][columna-1] == 0:
                             tablero [fila-1][columna-1]=ficha
                             return 


def dibujarTablero(tablero):
             for fila in range(7):
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
     return tablero


def validaSecuencia(secuencia):
    for columna in secuencia:
          if columna>7 or columna<1:
             return False
    return True


def contenidoColumna(nro_columna, tablero):
	columna=[]
	for fila in tablero:
		celda=fila[nro_columna-1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	return tablero[nro_fila]

def columnas(tablero):
	columnas=[]
	for indice in range(1, 8):
		columnas.append(contenidoColumna(indice,tablero))
	return columnas

def filas(tablero):
	return tablero


secuencia = [-1,1,2,3,1,31]
if validaSecuencia(secuencia):
   dibujarTablero(completarTableroEnOrden(tableroVacio(),secuencia))  
else:
   print('Secuencia Inválida - Los valores de las columnas deben estar entre valores del 1 al 7')


secuencia = [1,2,3,1]
if validaSecuencia(secuencia):
   dibujarTablero(completarTableroEnOrden(tableroVacio(),secuencia))  
else:
   print('Secuencia Inválida - Los valores de las columnas deben estar entre valores del 1 al 7')

print(contenidoColumna(2,tablero))

print("\n")

print(contenidoFila(6,tablero))

print("\n")

print(columnas(tablero))	

print("\n")

print(filas(tablero))


