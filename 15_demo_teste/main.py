"""

0 - 20

5 -> dados
5 ->  facil
7,5 -> accessíveis
2,5 -> dif

"""



def media(*nums):
    ct = len(nums)
    total = sum(nums)
    media = total / ct
    return media


# teste("Valor1", "Valor2")

# teste("prato 1", "prato 2", "prato 3")


res = media(12,11,15,12,13,11,41)
print(res)

res = media(12,11)
print(res)


def teste(**kwargs):
    print(kwargs["param1"])


teste(param1="val1", param2= "val2")


def teste2(*args, **kwargs):
    print(args)
    print(kwargs)


teste2(1,2,3,4, v1="val1", v2="val2")



def teste3(*args, **kwargs):
    print(args)
    print(kwargs)


teste2(1,2,3,4, v1="val1", v2="val2")



def novaFunc(p1, p2, p3):
    return print(p1, p2, p3)


novaFunc(3, p3=1, p2= 44)








def teste(**kwargs):
        if kwargs.__contains__("nome"):
            print("ola",kwargs["nome"])

        if "idade" in kwargs:
            print("tens",kwargs["idade"], "anos")


teste(nome="João")
teste(idade= 20)