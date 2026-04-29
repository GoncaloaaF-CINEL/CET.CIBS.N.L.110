from Carro import Carro

c = Carro("BMW", "320D", 2026)

print(c.marca)
print(c.modelo)
print(c.ano)

print("----")

"""
c.marca = "BMW"
c.modelo = "320D"
c.ano = 2026

print(c.marca)
print(c.modelo)
print(c.ano)
"""

c2 = Carro("Audi", "R8", 2026)
print(c2.marca)
print(c2.modelo)
print(c2.ano)

"""
c2.marca = "Audi"
c2.modelo = "R8"
c2.ano = 2026

print(c2.marca)
print(c2.modelo)
print(c2.ano)
"""
print("----")

c3 = Carro("Shelby", "GT500", 1967)
print(c3.marca)
print(c3.modelo)
print(c3.ano)

print("----")
print("----")

print(c2.ano)
c2.mudar_ano(2020)
print(c2.ano)

print("----")
print("----")
print("------")
lst = [c, c2, c3]

for i in lst:
    print(i.marca)



"""
Classe Bola: Crie uma classe que modele uma Bola: 
    Atributos: 
        - cor,
        - circunferência,
        - material

    Métodos:
        - trocaCor
        - mostraCor

"""

