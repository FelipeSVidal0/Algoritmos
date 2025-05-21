while True:
    print("1 - para cadastrar\n2 - para ler\n3 - para sair")
    a = input()
    if a == "1":
        with open("cadastro.txt", "a") as arquivo:          
            nome = input("Qual seu nome: ")
            gmail = input("Qual seu gmail: ")
            tel = (input("Qual seu telefone: "))
            lista = [nome, gmail, tel]
            for i in lista:
                arquivo.write(f"{i}\n")
    elif a == "2":
        with open("cadastro.txt","r") as arquivo:
            for i in arquivo:
                print(i, end="")
    else: 
        break