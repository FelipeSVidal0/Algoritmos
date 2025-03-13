# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite outro número: "))
# n3 = int(input("Digite outro número: "))

# lista = [n1, n2, n3]
# lista.sort()

# print(f"{lista[0]} < {lista[1]} < {lista[2]}")

lista = [5, 3, 4, 0, 9, 1, 2]
sim = True
moveu = False
i = 0
count = 0
while sim:
    
    if i+1 == len(lista):
        print(lista)
        i = 0
        if not moveu:
            sim = False
        else:
            moveu = False
            continue
    elif lista[i] > lista[i+1]:
        menor = lista[i+1]
        lista[i+1] = lista[i]
        lista[i] = menor
        moveu = True

    i += 1
    