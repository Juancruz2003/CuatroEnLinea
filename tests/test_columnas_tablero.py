from src.PrototipoPython import columnas

def test_columnas():
    tablero=[
                   [2, 0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 2, 0, 0, 0],
                   [2, 0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 2, 0, 0, 0],
                   [2, 0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 2, 0, 0, 0],
		   [2, 0, 0, 1, 0, 0, 0]              
                   ]
		
    assert [[2,1,2,1,2,1,2],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,2,1,2,1,2,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]==columnas(tablero)