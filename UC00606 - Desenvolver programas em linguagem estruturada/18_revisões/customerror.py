class IdadeInvalida(Exception):
    pass



def valIdade(idade:int):

    if idade < 18:
        raise IdadeInvalida("tem de ser maior de idade")
    else:
        return idade


try:
    valIdade(40)
    valIdade(14)
except IdadeInvalida as e:
    print(e)