"""

var
op com var

if
for
while
def
listas(arrays)
dict



TODO
sets

"""

my_set = {"valo1", "valo2", "valo3", "valo4"}
print(my_set)
print(my_set.__len__())

my_set.add("valo5") # add valores
print(my_set)
print(my_set.__len__())

my_set.add("valo5") # add valores
print(my_set)

print(my_set.__len__())

print(my_set.__contains__("valo5"))
print(my_set.__contains__("valo6"))
print("------------")
print("valo5" in my_set) # <=> my_set.__contains__("valo5")
print("valo10" in my_set)

print("------------")

resp1 = my_set.__contains__("valo5")
print(type(resp1))

resp2 = "valo10" in my_set
print(type(resp2))



# Crie um set com 4 ingrediente para um bolo
# adicione um novo ingrediente

# verifique se o bolo leva ovos

bolo = {"farinha", "açúcar", "canela", "leite"}
print(bolo)

# adicione un novo ingrediente
bolo.add("ovo")

print(bolo)

print("--------------------")

elm = "leite"
bolo.remove(elm) # se o valor nao Existir -> Erro

print(bolo)


"""
como criar
como add
como remover

como ver se está contido
"""

for elm in bolo:
    print(elm)
print("----------")

novo_set = {"fermento", "ovo", "maçã"}

bolo.update(novo_set)
print(bolo)


lst = [1,2,3,4,5,6,7,9]
print(type(lst), lst)

lst_set = set(lst)
print(type(lst_set), lst_set)

lst_set.add(31)

print(lst_set)

lst_set.add(31)

print(lst_set)




lst = [9, 9, 1,2,1,2,2,3,1,1,2,2]
print(type(lst), lst)

lst_set = set(lst)
print(type(lst_set), lst_set)


lst_set_lst = list(lst_set)
print(type(lst_set_lst), lst_set_lst)

lst.sort() # ordenar inplace
print(lst)

lst.sort(reverse=True) # ordenar inplace
print(lst)



print("--------set-----------")


set1 = {"Farinha", "Ovos", "Açúcar",  "Iogut", "Oleo"}
set2 = {"Açúcar", "Ovos", "Manteiga", "Farinha", "Leite"}


print("--")
print(set1.union(set2))
print(set2.union(set1))
print("--")
print(set1.intersection(set2))
print(set2.intersection(set1))
print("--")
print(set1.difference(set2))
print(set2.difference(set1))
print("--")

print(set1.symmetric_difference(set2))

