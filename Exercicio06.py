a = ['']*5

for i in range (len(a)):
    a[i]= int(input("Digite um número: "))
print(a)

for y in range (len(a)-1,-1,-1):
    print(a[y], end = " ")
