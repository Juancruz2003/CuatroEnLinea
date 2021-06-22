from src.PrototipoPython import validaSecuencia

def test_valida_secuencia():
    secuencia=[1,2,3,31,4]
		
    assert False==validaSecuencia(secuencia)