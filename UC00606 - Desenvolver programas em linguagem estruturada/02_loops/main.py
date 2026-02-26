# faça ping a 100 endereços seq


ip_inicial = 2  # ( 2 ao 102)

# mostar os num de 1 a 10
num = 1
while num <= 10:  # Enquanto  num <=  10 fazer
    print(num)
    num += 1
    pass  # serve para não dar erro

# mostar os num de 5 a 25
print("-------------")

num = 5
while num <= 25:
    print(num)
    num += 1

# mostar os num de 25 a 5
print("-------------")
num = 25

while num >= 5:
    print(num)
    num -= 1

# mostre a tabuada do 7
print("-------------")
num = 1
tab = 7

while num <= 10:
    res = num * tab
    print(f"{tab} x {num:2} = {res}")
    num += 1

# mostre a tabuada de um valor pedido ao utilizador
print("-------------")

num = 1
tab = int(input("Queres ver a tabuada de que valor:  "))

while num <= 10:
    res = num * tab
    print(f"{tab} x {num:2} = {res}")
    num += 1

# mostre a tabuada de um valor pedido ao utilizador, valide que o valor inserido esta entre 0 e 10
# se o valor for invalido não faça nada

print("-------------")

num = 1
tab = int(input("Queres ver a tabuada de que valor(0-10):  "))

if tab >= 0 and tab <= 10:
    while num <= 10:
        res = num * tab
        print(f"{tab} x {num:2} = {res}")
        num += 1

print("-------------")

num = 1
tab = int(input("Queres ver a tabuada de que valor(0-10) v2:  "))

if 0 <= tab <= 10:
    while num <= 10:
        res = num * tab
        print(f"{tab} x {num:2} = {res}")
        num += 1
