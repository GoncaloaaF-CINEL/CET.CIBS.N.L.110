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

"""

range(n) -> todos os int de 0 ate n-1  -> [0, n[

range(m, n) -> todos os int de m ate n-1  -> [m, n[

range(m, n, s) todos os int de m ate n-1 com step de s


"""

print("-------------")

num = 1
tab = int(input("Queres ver a tabuada de que valor(0-10) v3:  "))

if tab in range(0, 11):
    while num <= 10:
        res = num * tab
        print(f"{tab} x {num:2} = {res}")
        num += 1

print("------------")
tab = int(input("Queres ver a tabuada de que valor (0-10)? "))
if tab < 0 or tab > 10:
    print("Número inválido")
else:
    num = 1
    while num <= 10:
        print(tab, "x", num, "=", tab * num)
        num = num + 1

# mostre todos os num par entre 0 e 100
print("-------------")
num = 0
while num <= 100:
    print(num)
    num += 2

# com range


print("......-------------")

n = 0  # 0 é par

while n in range(0, 100, 2):  # -> com um for e top
    print(n)
    n += 2

# sem range

n = 0
n2 = 0
while n <= 100:
    if n % 2 == 0:
        print(n)
        n += 2

# mostre todos os num par entre n e m (n e m são pedidos ao utilizador)

# sem range - mais simples


#############################################
# for
#############################################

# mostre todos os num par entre 0 e 100
# range

for num in range(0, 100, 2):
    print(num)

for num in range(0, 100, 2):  # nao mexer aqui
    print(num)
    if num == 20:
        break  # tremina o loop

# for vs while

# faça um programa que peça num a usr, qd foi inserido um número negativo o programa pàra
# while


# faça um programa que peça até 50 num, se o usr inserir um número negativo o programa pàra
# for
