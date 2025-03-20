# Puxa a função randint da bibloteca random
from random import randint

#Declara a Variável (s)
s = 0

#Cria um loop com um raio de 10 números
for i in range(10):

    #Declara a Variável (n1) para os valores aleatórios
    n1 = randint(0, 10)

    #Mostra na tela o valor de (n1)
    print(n1)

    #Declara (s) como += á (n1)
    s += n1

#No final mostra na tela o valor da Média
print(f"A média é {s}")