"""

r
w
a
x - Create

"""


with open("teste5.txt", "a") as f:
    pass
    # f.write("linha 1\n")
    # f.write("linha 2\n")
    # f.write("linha 3\n")



with open("teste5.txt", "r") as f:
    print(f.readline(), end= "")
    print(f.readline(), end= "")
    print(f.readline(), end= "")
    print(f.readline(), end= "")

print("-------------")
with open("teste5.txt", "r") as f:
    print(f.readlines()[2])

print("-------------")

with open("teste5.txt", "r") as f:
    print(f.read(300))

print("-------------")
