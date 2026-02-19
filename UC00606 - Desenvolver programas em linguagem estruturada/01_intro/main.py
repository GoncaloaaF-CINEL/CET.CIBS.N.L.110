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


# loops
