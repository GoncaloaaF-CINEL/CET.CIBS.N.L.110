import random

##pos   0  1   2   3   4  5   6  7    8  9

lst = [17, 4, 92, 31, 56, 8, 73, 45, 60, 12]

print(lst[0])

print(lst[5])

# print(lst[91]) <- se o idx não existe -> Erro

print(lst[9])

print(lst)

## print(lst[91])


lst = [17, 4, 92, 31, 56, 8, 73, 45, 60, 12]

lst[0] = 99
print(lst)

lst.append(88)  # add sp no final da lista
print(lst)

lst.insert(1, 66)
print(lst)

## num de elm na lista
print(len(lst))
print(lst.__len__())

# Criar lista
# aceder a elm
# modificar elm
# add elm
# len

# remover
## pop remove por idx
print(lst)
print(lst.pop())
print(lst)

print(lst.pop(0))
print(lst)

# print(lst.pop(999)) # se não exitir -> erro
# print(lst)

## pop remove por valor
print(lst.remove(66))
print(lst)

# print(lst.remove(66)) # se não exitir -> erro
# print(lst)


# itr por listas

for elm in lst:
    print(elm, end='\t')

"""
1. Faça um Programa que paça 5 números inteiros ao utilizador e adicione esse num a uma lista.
    mostre a lista na consola.
"""

"""
1.1 Faça um Programa que paça N números inteiros ao utilizador e adicione esse num a uma lista.
    mostre a lista na consola.
    
    o valor N deve ser fornecido 
"""
print("------------------")
n = 0
list_num = []

for i in range(1, n + 1):
    num = int(input(f"Digite o {i}º numero: "))
    list_num.append(num)

print(list_num)

for num in list_num:
    print(num)

print("------------------")
"""
Faça um Programa com uma lista com 5 números inteiros e metre-os na ordem inversa.
"""

lst = [5, 4, 3, 2, 1]

## lst.reverse()
print(lst)
print("------------------")

list_size = len(lst)
for i in range(1, 6):
    print(lst[list_size - i])

print(lst)

print("------------------")

nomes = [
    "Ana", "Bruno", "Carla", "Diogo", "Eduardo",
    "Filipa", "Gonçalo", "Helena", "Inês", "João",
    "Luís", "Marta", "Nuno", "Olga", "Pedro",
    "Rita", "Sofia", "Tiago", "Vasco", "Beatriz",
    "Daniel", "Fábio", "Leonor", "Miguel", "Patrícia"
]

print(nomes[1])

print(nomes[1:5])

print(nomes[0:5])

print(nomes[:5])

print(nomes[20:])

print(nomes[:])

# faça o print do último elemento da lista

last = len(nomes) - 1
print(nomes[last])

print(nomes[-5])

print(nomes[-10:-5])

# print(nomes[-50]) # -> tb da erro


print("-------")
print(nomes[:5])
print(nomes[5:])
"""
print(nomes[a:b:c])

a - inicio
b - fim
c - step (direção, se >0 "->" se < 0 "<-" )
"""
print(nomes[5::-1])

print("---------")

lst = [5, 4, 3, 2, 1]

print(lst[::-1])
print(lst)

print("--------------")

print("-----------------------")

print(nomes[5::-1])
print(nomes[5::4])

print(nomes[5::4])

print(nomes[5:20:2])

print(nomes[20:5:-2])

print("-----------------------")

"""
dado a lista:

nomes = [
    "Ana", "Bruno", "Carla", "Diogo", "Eduardo",        # 0 ao 4
    "Filipa", "Gonçalo", "Helena", "Inês", "João",      # 5 ao 9
    "Luís", "Marta", "Nuno", "Olga", "Pedro",           # 10 ao 14
    "Rita", "Sofia", "Tiago", "Vasco", "Beatriz"        # 15 ao 19
    "Daniel", "Fábio", "Leonor", "Miguel", "Patrícia"   # 20 ao 24 
]

mostre uma sub lista so nomes nos index par 

mostre a sub lista dos pares na ordem inversa 
"""

print(nomes[::-2])

"""
Faça um Programa que leia uma palavra de 10 caracteres, e diga quantas consoantes foram lidas. 
guarde as consoantes numa lista. No final Imprima as consoantes.

consoantes <=> nao vogal

Extra: validar se a palavra tem 10 caracteres
"""

# var como vogais

vogais = "aeiou"  # ["a", "e", "i", "o", "u"]

# lista consoantes
consoantes = []

# ler a palavra

palavra = input("Digite uma palavra com 10chars: ")

# validar e são so letras
# validar se tem 10 caracteres

if palavra.isalpha() and palavra.__len__() == 10:
    print("Palavra:", palavra)

else:
    print("Palavra invalida:", palavra)

# print(random.randint(1, 6))  # <- para gerar num random

# txt = "eqweqwe"
# print(txt.isalpha())  # ver ser todos os chars são letras

"""
Faça um programa que simule um lançamento de dados. 
Lance o dado N vezes e armazene os resultados numa lista.
Depois, mostre quantas vezes cada valor foi conseguido. 
 
Dica: use um lista de contadores(1-6) e uma função para gerar números aleatórios,
  simulando os lançamentos dos dados.


calcule a percentagem de vezes que cada num saiu
"""

n = 100
saidas = [0, 0, 0, 0, 0, 0]
for _ in range(n):
    num = random.randint(1, 6)
    saidas[num - 1] += 1

print(saidas)
"""
var 
op var
condições 
    if
    elif
    else

loops
    for 
    while
    
funcs 
    def
    
collections 
    listas

"""
