//Puxa a Biblioteca do C para mostrar informação na tela
#include <stdio.h>

int main() {
    //Declara a variável "sm" e define ela com valor 0 (float = Número com vírgula) 
    float sm = 0;
    //Abre um loop que vai pedir 10 números para fazer a média de 2 em 2 somando-os
    for (int i = 0; i < 10; i++)
    {
        //Declara a Variável (n)
        float n;
        //Diz: se i for menor que 1 ele vai pedir um número
        if (i < 1)
        {
            //Mostra a mesnsagem
            printf("Digite um número:\n");
            //Pede um número
            scanf("%f", &n);
            //Declara (sm) e faz com que o valor dele some e atualize com (n)
            sm += n;
        }
        //Diz que se i não for menor q 1 ele pede outro número,soma ele e divide por 2
        else
        {
            //Mostra a mensagem
            printf("Digite outro número: \n");
            //Pede outro número
            scanf("%f", &n);
            //Declara que (sm) é igual a soma do "sm + n" e divide por 2
            sm = (sm + n) / 2;
        }
        //A cada número é mostrado na tela a nova média
        printf("A média é: %.1f\n", sm);
    
    }
return 0;

    
}