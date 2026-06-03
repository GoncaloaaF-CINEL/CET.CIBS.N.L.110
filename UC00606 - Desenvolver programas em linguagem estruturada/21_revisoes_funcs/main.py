


def nome():
    print("ola mundo")

nome()


def msg(nome_usr: str):
    nome_usr = nome_usr.capitalize()
    print(f"ola mundo, {nome_usr}")


msg("Gonçalo")
msg("gONCALO")



def msg2(nome_usr: str):
    nome_usr = nome_usr.capitalize()
    return f"ola mundo, {nome_usr}"

print("------")
m = msg2("Joao")

print(m)

print("------")


def teste(lst:list[int]):
    print(lst)


teste([1,3,4,1,4,5,5])