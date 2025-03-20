#Declara variável
s = 0

#Cria um loop de 10 interações, pede 10 números e soma eles
for i in range(10):
    n1 = int(input("Digite um número: "))
    s += n1

#Divide o valor por 10 e mostra o resultado
s /= 10
print(f"A média é {s}")