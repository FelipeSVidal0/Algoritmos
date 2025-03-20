# Puxa a função randint da bibloteca random
from random import randint

# Declara uma lista vazia
lista = []

# Cria e adiciona na lista 100 números aleatórios, os números vão de 0 a 1000
for i in range(100):
    n = randint(0, 1000)
    lista.append(n)

# Declara variáveis para o algoritmo
sim = True
moveu = False
i = 0

# Enquanto sim for verdade, o código irá se repetir
while sim:
    '''
    i é a variável de controle do loop, caso ela esteja na ultima iteração, ao invés de continuar o loop, 
    irá verificar se há elementos sendo movidos na lista, em caso negativo,
    ele termina o loop. Caso haja movimentos, ele continua o loop, recomeçando ele
    '''

    if i+1 == len(lista):
        print(lista)
        i = 0
        if not moveu:
            sim = False
        else:
            moveu = False
            continue
    # verifica se o número da esquerda é maior que o da direita, caso seja, eles são trocados de lugar. E sinaliza que houve mudanças na ordem dos números (moveu = True)
    elif lista[i] > lista[i+1]:
        menor = lista[i+1]
        lista[i+1] = lista[i]
        lista[i] = menor
        moveu = True    
    # Incrementa 1 em i
    i += 1   