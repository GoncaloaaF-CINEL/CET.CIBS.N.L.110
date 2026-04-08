lista = [1, 2, 3, 4, 5]

lista.append(31)
print(lista[0])
print(lista[1])

my_dict = {
    "nome": "Gonçalo",
    "escola": "CINEL",
    "ano": 2025,
    "estado": True
}

print(my_dict)

print(my_dict["nome"])
print(my_dict["ano"])

print(my_dict["estado"])

my_dict["estado"] = False

print(my_dict["estado"])

lista = {
    3: "Gonçalo",
    4: "CINEL",
    5: 2025,
    6: True
}

print("------")
print(lista[3])

my_dict = {
    "nome": "Gonçalo",
    "escola": "CINEL",
    "ano": 2025,
    "estado": True
}

my_dict["nova Key"] = "Novo valor"
print(my_dict)

print(my_dict.get("nome"))  # <=> my_dict["nome"]

print(my_dict.get("key Invalida", "sem valor"))

print(my_dict.pop("nome"))  # remove e deolve o valor

print(my_dict)

# print(my_dict.pop("nome111"))  # se nao existe -> erro


print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print("----------")
for elm in my_dict:
    print(elm)

print("----------")
for elm in my_dict.values():
    print(elm)

print("----------")
for elm in my_dict.items():
    print(elm)

"""

Crie um programa que leia uma frase, e conte o número de vezes que cada consoante aparece.

"""

"""
Dada a lista:

alunos = [
    {"nome": "Ana", "nota": 18},
    {"nome": "Rui", "nota": 9},
    {"nome": "João", "nota": 12}
]
Pede:
Mostrar todos os nomes
Mostrar só os aprovados (nota >= 10)
Calcular a média das notas

"""

"""
Cria um programa que:
    Leia várias notas (0 a 20) separadas por espaço: Classifique cada nota como:
        "Reprovado" (<10)
        "Suficiente" (10-13)
        "Bom" (14-17)
        "Muito Bom" (18-20)
        
    Conte quantas notas existem em cada categoria
    Guarde o resultado num dicionário
    Mostre o resultado
💡 
Exemplo
Input: 12 15 8 19 10

Resultado:
Reprovado: 1
Suficiente: 2
Bom: 1
Muito Bom: 1

"""
