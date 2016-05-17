#include <stdio.h>
#include <stdlib.h>

int main() {
    int* arr = (int*)calloc(10, sizeof(int));
    int i;
    for (i = 0; i < 10; i++) {
        arr[i] = i;
    }

    for (i = 0; i < 10; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}
