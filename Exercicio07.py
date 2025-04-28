nome = ['']*5
senha = ['']*5

for x in range (len(nome)):
    nome[x]= input("Digite seu nome: ")
print(nome)
print("________________________________")
for y in range (len(senha)):
    senha[y] = int(input("Digite sua senha: "))
print(senha)
print("________________________________")
print(f"Nome: {nome}, Senha: {senha}, está na posição {y}")
