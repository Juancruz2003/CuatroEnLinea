from src.PrototipoPython import contenidoFila

def test_contenido_fila():
    tablero=[
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [2, 2, 2, 1, 1, 1, 1],
                   [2, 2, 1, 1, 1, 1, 2],
                   [2, 1, 1, 1, 1, 2, 2],
                   [1, 1, 1, 1, 2, 2, 2]                   
                   ]
		
    assert [2,2,2,1,1,1,1]==contenidoFila(4,tablero)