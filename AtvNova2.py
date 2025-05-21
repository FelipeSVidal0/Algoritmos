#pede um inteiro de vezes que quer deixar em looping(n)
n = int(input())

#pedir um numero inteiro (a)
a = int(input())

#pede outro numero inteiro(b)
b = int(input())

#soma a e b em (x1)
x1 = a + b 

#cria uma lista para colocar os resultados(resultados), no qual começa recebendo x1
resultado = [x1]

#cria uma variavel com o valor 0 (soma)
soma = 0 

#criar um looping com n -1, com (i) a variavel que vai percorrer
for i in range(n-2):
    #pede um número inteiro(numero)
    numero = int(input())
    #se i for impar
    if i % 2 == 1:
        #numero vai se somar com x1
        x1 += numero
    #se for par 
    else:
        #numero vai multiplicar com x1
        x1 *= numero
    #resultado vai receber os valores de x1
    resultado.append(x1)

#imprime x1
for i in resultado:
    soma += i
print(soma)
