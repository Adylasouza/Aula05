arrayAlunos = ['Adyla','Marcos','Marrocos','Feijocos','Cheirosos']
"""for x in range (len(arrayAlunos)):
    arrayAlunos[x]=input("Digite o nome de 5  alunos:  ")"""
verificacao = input("Digite um nome: ")
for x in range (len(arrayAlunos)):
    if verificacao == arrayAlunos[x]:
        print(f"Nome {arrayAlunos[x]}, está na posição {y}")
    else:
        print("Nome não se encontra na lista!!")