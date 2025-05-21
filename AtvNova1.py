#pedir uma str(palavra) pro usuario
palavra = input()
#criar variaveis para pegar a quantidade de vogais(qtdA, qtdE..., qtdU)
qtdA = 0
qtdI = 0
qtdE = 0
qtdO = 0
qtdU = 0
#percorrer palavra com a variavel(i)
for i in palavra:
    #se i for igual a A ou a:
    if i == "A" or "a":
        #soma 1 em qtdA
        qtdA += 1
        
    #se i for igual a E ou e:
    if i == "E" or "e":
        #soma 1 em qtdE
        qtdE += 1
    #se i for igual a I ou i:
    if i == "I" or "i":
        #soma 1 em qtdI
        qtdI+= 1
    #se i for igual a O ou o:
    if i == "O" or "o":
        #soma 1 em qtdO
        qtdO += 1
    #se i for igual a U ou u:
    if i == "U" or "u":
        #soma 1 em qtdU
        qtdU += 1
#imprima qtdA, qtdE, qtdI, qtdO, qtdU
print(qtdA, qtdE,qtdI, qtdO, qtdU)
