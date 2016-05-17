/** 
 * environ is a global var under c programming environment.
 * it's an array containning pointers.
 * we can use getenv/putenv to get a specific env value.
 * some place not standard, environment variable would be passed as the third arg of main func.
 *
 */


#include <stdio.h>
#include <stdlib.h> // for putenv/getenv

extern char** environ;

int main() {
    putenv("MyKey=MyVal");
    printf("MyKey:%s\n", getenv("MyKey"));

    // retrieve all env key/value s
    printf("below, we gota to iterate over all env key/value s\n");
    char** cur = environ;
    while (*cur != NULL) {
        printf("%s\n", *cur);
        cur++;
    }
    return 0;
}
