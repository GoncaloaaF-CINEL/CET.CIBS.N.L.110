aluno = ("Rui", 18)

print(aluno[0])
print(aluno[1])



def mudar_media(aluno: tuple, nova_media: float):
    al = list(aluno)
    al[1] = nova_media
    return tuple(al)


print(aluno)
aluno = mudar_media(aluno, 19)

print(aluno)

aluno = ("Rui", 18)
nome, media = aluno

print(f"Nome: {aluno[0]} tem media de {aluno[1]}")
print(f"Nome: {nome} tem media de {media}")

"""
Foram anotadas as idades e alturas de 30 alunos. 


Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura
inferior à média da altura de todos os alunos e inferior a media dos alunos com 13 anos.

"""