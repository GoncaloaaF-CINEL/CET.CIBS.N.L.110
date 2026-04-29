from Carro import Carro

c = Carro()

print(c.marca)
print(c.modelo)
print(c.ano)

c.marca = "BMW"
c.modelo = "320D"
c.ano = 2026

print(c.marca)
print(c.modelo)
print(c.ano)

c2 = Carro()
print(c2.marca)
print(c2.modelo)
print(c2.ano)

c2.marca = "Audi"
c2.modelo = "R8"
c2.ano = 2026

print(c2.marca)
print(c2.modelo)
print(c2.ano)

print("------")
lst = [c, c2]

for i in lst:
    print(i.marca)



"""
Classe Bola: Crie uma classe que modele uma Bola: 
    Atributos: 
        - cor,
        - circunferência,
        - material

"""

