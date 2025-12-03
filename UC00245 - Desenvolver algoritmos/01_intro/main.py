# comt

"""
comt
com
mais
de
uma
linha
"""

"""
/n -> muda de linha
/t - Tab
/f - paragrafo

\" - > "
\\ -> \
"""

# mostrar msg ao user

print("ola\nMundo")
print("ola\tMundo 2")
print("ola\fMundo 3")

# ola Mundo 3: "Gonçalo"
print(' ola Mundo 3: "Gonçalo" ')

print("ola Mundo 3: \"Gonçalo\"")

# var

nome = "Gonçalo"  # String -> str
print(nome)

nome = 12
print(nome)
"""

int - inteiro 
float - decimal
str - texto 
bool - T / F

"""

# type hint
idade: int = 20
print(idade)

idade = 23
print(idade)

idade = "Gonçalo"
print(idade)

# receber inputs do user

nova_var_com_nome_cool = input("nome: ")  # devolve sempre str
print(nova_var_com_nome_cool)

# faça uma app py linha de comandos que some 2 números inteiros

num1 = int(input("num1: "))
num2 = int(input("num2: "))
soma = num1 + num2

print("a soma é", soma)
print("a soma é " + str(soma))
print(f"a soma é {soma}")

print(f"a soma de {num1} com {num2} é {soma}")

nome = input("Digite o nome: ")
print(f"o nome digitado foi: {nome}")  # f-string

# if


# while
