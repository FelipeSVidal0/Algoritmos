#include <stdio.h>

int main() {
    int nums[] = {};
    for (int i = 0; i < 3; i++) {
        int n;
        printf("Digite um número: ");
        scanf("%d", &n);
        nums[i] = n;
        printf("%d\n", nums[i]);
    }
    int menor, intermediario, maior;

    return 0;
