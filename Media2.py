#Define a variável (s) com o valor de 0
s = 0

#Cria um loop com um raio de 10
for i in range(10):

    #Diz que se i for menor que 1, vai pedir um número
    if i < 1:

        #Declara (n1) e entrega para ele o valor do input(entrada) e a mensagem
        n1 = int(input("Digite um número: "))

        #Declara o valor de (s) e faz com que o valor dele some e atualize com (n1)
        s += n1

    #Diz que se i não for menor q 1 ele pede outro número, soma ele e divide por 2
    else:

        
        n1 = int(input("Digite outro número: "))
        s += n1 
        s /= 2

        #Atualiza o valor da média (s) na tela
        print(f'A média de agora é {s}')


#Mostra a média final na tela
print(f"A média é {s}")