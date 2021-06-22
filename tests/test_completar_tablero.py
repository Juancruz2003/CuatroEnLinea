from src.PrototipoPython import completarTableroEnOrden

def test_soltar_completar_tablero():
    tablero=[
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0]              
                   ]
    secuencia=[1,2,3,4,5,6,7]
		
    assert [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,2,1,2,1,2,1]]==completarTableroEnOrden(tablero,secuencia)