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
