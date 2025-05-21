# criar listas com palavras
port = ["como", "oi", "bonito", "azul"]
ing = ["how", "hello", "beautiful", "blue"]

# inicializa a variável de tradução
traducao = ""

# solicitar uma string (palavra)
palavra = input("Digite uma palavra em português: ").lower()

# percorrer a lista port com índice
for i in port:
    if palavra == port[i]:
        traducao = ing[i]
        break  # sai do loop assim que encontra

# imprimir a tradução
if traducao:
    print("Tradução para o inglês:", traducao)
else:
    print("Palavra não encontrada.")
