
print("inicio do código")


lst = [1,2,3]

try:
    print("inicio try")
    lst[55]
    print("fim try")
except IndexError as e:
    print(f"Erro no Index: {e}")
finally:
    print("é executado sempre")

print("fim do código")