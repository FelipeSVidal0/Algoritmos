#criar o campo minado
campoMinado = [
    [0,0,0,1,1,1,],
    [1,1,1,1,2,1,],
    [1,2,1,1,1,1,],
    [1,1,1,0,0,0,],
    [0,0,1,1,1,0,],
    [0,0,1,2,1,0]
]

x = int(input("Escreva o x"))
y = int(input("Escreva o y"))

valor = campoMinado[x][y]

if valor == "0":
    print("nao ha bombas por perto")
elif valor == "1":
    print("ha bombas por perto")
else:
    print("KABUMMM")