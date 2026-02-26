# var

nome = "Gonçalo"  # str -> txt
# print(nome)

nome = 1234  # int <- EVITAR, NÃO FAZER
# print(nome)

# <- Comentário, é ignorado
"""
comt
multi 
linha
"""

nome = "Gonçalo"  # <-- str
ano = 2026  # <-- int
peso = 50.5  # <- double
aprovado = True  # <- bool -> True ou False

data = "...."  # <- Date -> data
data_e_hora = "22/Jan/2019:03:56:14 +0330"  # <- DateTime -> data e hora
time = ""  # time -> hora

# print

print(nome)
print("Ola Mundo " + nome)
print("Ola Mundo", nome)
print(f"Ola Mundo {nome}")

# print("ano " + ano) <- erro pq nao podem somar txt com num

print("ano " + str(ano))
"""
int     ->   str
10      ->  "10"
str(10) ->  "10"

int("10") ->  10

int("1r") ->  Erro
"""

print("ano", ano)
print(f"ano {ano}")

# condições

# if
if aprovado:
    print("dentro do if")
    print("aprovado")
    print("ainda dentro do if")

else:
    print("nao aprovado")

nota = 10

if nota >= 10:
    print("aprovado")
elif nota > 8:
    print("porva oral")
else:
    print("nao aprovado")
"""
nota = input("informe uma nota: ")  # lido sp como str
# para fazerem op -> converter s str para int

nota = int(nota)

# exp validar se é uma nota valida (0 a 10)

if nota >= 10:
    print("aprovado")
elif nota > 8:
    print("porva oral")
else:
    print("nao aprovado")
"""
# loops


# for


# while


"""

10 11 12 13 14 15 16 17 18 19 20 -> aprovado (nota >= 10)

8 9  -> prova oral -> aprovado (nota >= 8) )

0 1 2 3 4 5 6 7 -> reprovado (nota <= 7 )

"""

print("----------------------------------------")
print("----------------------------------------")

nota = 14

if nota >= 10:
    print("Aprovado")
else:  # elif nota < 10:  # -> nota < 10
    print("Reprovado")

print("----------------------------------------")
print("----------------------------------------")

nota = 14

if nota >= 10:
    print("Aprovado")

elif nota > 8:
    print("prova oral")

else:  # elif nota < 10:  # -> nota < 10
    print("Reprovado")

print("...................................")
print("...................................")

num = 25

# se num == 20
if num == 20:
    print("Ok")
else:  # senão
    print("o valor não e 20")

"""

se um num for 30 deve imprimir "o valor é 30"

se nao for 30 deve informar: "o valor é diferente de 30"

"""

"""

== -> eq 
>  -> gr 
<  -> lo
>= -> gt
<= -> lt


informe se um aluno esta aprovado ou não.
critérios de aprovação: nota maior ou igual a 10
 

informe se uma pessoa e um adulto.

"""

idade = 20

if idade >= 18:
    print("Adulto")
else:
    print("menor")

"""

indique se um porduto e caro ou barato, pode considerar caro se custar mais de 100 euros 

"""

"""

indique se uma pessoa e tem peso a mais, considere que acima de  80k tem peso a mais 

"""

"""

indique se uma pessoa  e alta considere que acima de  1.76 é alta 

"""
