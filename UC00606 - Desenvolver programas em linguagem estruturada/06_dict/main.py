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
