from src.PrototipoPython import tableroVacio

def test_tablero_vacio_tiene_7_filas():
    tablero = tableroVacio()

    assert len(tablero) == 7