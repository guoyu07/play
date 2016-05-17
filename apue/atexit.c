#include <stdio.h>
#include <stdlib.h> //for exit and atexit

static void my_exit1() {
    printf("first registered atexit func!\n");
}

static void my_exit2() {
    printf("second registered atexit func!\n");
}

int main() {
    if (atexit(my_exit2) != 0) {
        printf("can't reg my_exit2!\n");
        exit(1);
    }

    if (atexit(my_exit1) != 0) {
        printf("can't reg my_exit1!\n");
        exit(2);
    }

    printf("main is done!\n");
    return 0;
}
