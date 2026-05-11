

def criar_log():
    def interna(func):
        def wrapper(*args, **kwargs):
            print("antes")
            resultado = func(*args, **kwargs)
            print("depois")
            return resultado
        return wrapper
    return interna


@criar_log()
def login(estado:bool):
    return estado

@criar_log()
def acederDB(estado:bool):
    return estado



login(True)
