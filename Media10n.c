#include <stdio.h>

int main(){

    //Declara as variáveis
    int i;
    int s = 0;

    //Cria um loop de 10 interações, que pede um número e soma eles
    for (i = 1; i < 11; i++) {
        printf("Digite um número nº%d\n", i);
        int n;
        scanf("%d", &n);
        s += n;
        printf("A soma é igual a: %d\n", s);
    }

    //Cálcula a média e mostra o resultado
    int m = s /10;
    printf("A média é: %d\n", m);
    return 0;
}