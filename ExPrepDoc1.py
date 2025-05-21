from random import sample
lista = [] 
with open("sla.txt", "w") as arquivo:
    numero = sample(range(0, 1000000),50000)
    for j in numero:
        arquivo.write(f"{j}\n")

        lista.append(j)

n = len(lista)

with open("sla.txt", "w") as arquivo:
    for i in range(n):
        for k in range(0, n-i - 1):
            if lista[k] > lista[k+1]:
                lista[k], lista[k+1] = lista[k+1], lista[k]
    for j in lista:   
        arquivo.write(f"{j}\n")
        