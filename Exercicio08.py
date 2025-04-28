usuarios = ['Joao','Carlos','Mario','Maria','Josefa']
senhas = [1234,3432,5432,3333,6666]

login = input("Digite seu nome: ")
password = int(input("Digite sua senha: "))
for i in range(len(usuarios)):
    if login == usuarios[i] or password==senhas:
        print("Login efetuado com sucesso!")
    else:
        print("Login não efetuado!")
