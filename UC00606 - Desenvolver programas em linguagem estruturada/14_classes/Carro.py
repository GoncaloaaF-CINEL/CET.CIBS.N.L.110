
class Carro:
    """
    marca
    cv
    cc
    num portas
    etc etc etc

    -----
    marca
    modelo
    ano

    """

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mudar_ano(self, novo_ano):
        self.ano = novo_ano