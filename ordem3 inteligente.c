#include <stdio.h>

int main() {
    int nums[3];
    for (int i = 1; i < 4; i++) {
        int n;
        printf("Digite um número: ");
        scanf("%d", &n);
        nums[i] = n;
        printf("vetor %d = %d\n", i, nums[i]);
    }
    int menor, intermediario, maior;

    return 0;
} 