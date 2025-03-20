//Inclui as Bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    //Declara as Variáveis
    float s = 0;
    int i;
    //Usado para gerar uma Seed(Semente) aleatória
    srand(time(NULL));

    //Abre o Loop dos 10 Números aleatórios
    for ( i = 0; i < 10; i++)
    {
        //Declara a variável (n) para o rand
        float n =rand() % 11;
        //Mostra na tela o Valor dos 10 números
        printf("%.1f\n", n);
        //Declara (s) += á (n)
        s += n;
    }
    //Declara a Variável (m) com o Valor de (s) dividido por 10
    float m = s / 10;
    //Mostra na tela o valor da Média
    printf("A média é: %.1f\n", m);
    //Termina o código
    return 0;
}