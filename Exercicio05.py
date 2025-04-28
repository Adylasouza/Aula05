'''vetorA= ['']*5
valor = 0
multi = 0


for x in range (len(vetorA)):
    vetorA[x] = float(input("Digite a número: "))
print("_____________________________________________")
valor = input("Insira o valor multiplicador: ")

for m in range (len(vetorA)):
  vetorB = ['']*5
  vetorB = valor*vetorA[x]
  print(vetorB)
'''

a=['']*5
m= ['']*5
x= 0
for i in range(len(a)):
    a[i] = int(input("Digite um número:  "))
print("___________________________________________")

x = int(input("Digite o multiplicador: "))
print("_________________")
for y in range(len(m)):
    m[y] = x*a[y]
print(a)
print("_________________")
print(x)
print("_________________")
print(m)
