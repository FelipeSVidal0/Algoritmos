from random import sample
lista = [] 
with open("sla.txt", "w") as arquivo:
    numero = sample(range(0, 1000000),50000)
    for j in numero:
        arquivo.write(f"{j}\n")
        lista.append(j)
        
with open("sla.txt", "w") as arquivo:
    a = sorted(lista)
    for j in a:
        arquivo.write(f"{j}\n")
        