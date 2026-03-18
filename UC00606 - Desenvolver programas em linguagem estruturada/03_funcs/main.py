"""

var
op com var

if
while
range
for

"""


def teste():
    print("Ola Mundo")


teste()
teste()


def ola_mundo(nome: str):
    print(f"Ola Mundo, {nome}")


ola_mundo("Gonçalo")
ola_mundo("Ana")
ola_mundo("Rita")


def calc_tabuada(tabuada: int):
    if 0 > tabuada or tabuada > 10:
        print("Tabuada invalida!")
        return

    for i in range(1, 11):
        resp = tabuada * i
        print(f"{i} x {tabuada} = {resp}")


calc_tabuada(3)
print("----")
calc_tabuada(9)
print("----")

calc_tabuada(-1)


def calc_tabuada2(tabuada: int, max_tab: int = 10):
    print("----")
    if 0 > tabuada:
        print("Tabuada invalida!")
        return

    for i in range(1, max_tab + 1):
        resp = tabuada * i
        resp = tabuada * i
        print(f"{i} x {tabuada} = {resp}")

    print("----")


calc_tabuada2(3, 10)

calc_tabuada2(4, 15)

calc_tabuada2(9)


def soma(num1: int, num2: int) -> int:
    return num1 + num2


print(soma(4, 5))

resultado = soma(19, 3)

# código e mais código

print(resultado)

resultado2 = soma(resultado, 10)
print(resultado2)


def msg():
    pass  # cria um bloco vazio


def msg2(nome: str, escola: str = "CINEL", ano: int = 2026):
    return f"Ola {nome} no ano {ano} estudas na escola {escola}"


print(msg2("Gonçalo"))

print(msg2("Gonçalo", "IEFP"))

print(msg2("Gonçalo", "IEFP", 2000))

print(msg2("Gonçalo", ano=1998))

print(msg2("Gonçalo", ano=2019))

print("Ola Mundo")
print("Ola Mundo", end=" ")
print("Ola Mundo2")
print("-------------------")

print("txt1", "txt2", sep="-")
print("txt1", "txt2", sep="\t")
"""
1 Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    
    para um n informado pelo usuário.
     Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 
    
"""


def ex1(n: int):
    pass


"""
2 Faça um programa para imprimir:  for -> for

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    
    para um n informado pelo usuário.
     Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 
    
"""
"""

3 - Faça um programa, com uma função que necessite de três argumentos, 
    e que forneça a soma desses três argumentos.

4 - Faça um programa, com uma função que necessite de um argumento. 
    A função retorna ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

5 - Faça um programa com uma função chamada somaImposto. 

    A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto 
    sobre vendas expressa em percentagem e custo, que é o custo de um item antes do imposto. 
    
    A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
