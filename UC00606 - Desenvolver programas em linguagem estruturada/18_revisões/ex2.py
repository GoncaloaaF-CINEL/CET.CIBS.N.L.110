
try:
    n1 = int(input("valor1: "))
    n2 = int(input("valor2: "))

    res = n1 / n2
    print(res)

except ValueError as e:
    print(f"Os valors nao são inteiros ")
    # criar um log

except ZeroDivisionError as e:
    print("Impossivel dividir por 0")
    # criar um log

except Exception as e:
    print("Ocorreu um erro generico")
    # criar um log

else:
    print("e executado qd não ha erros")
    # criar um log 

finally:
    print("E executado sempre")



# ValueError
# ZeroDivisionError