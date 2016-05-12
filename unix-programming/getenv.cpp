#include <cstdio>
#include <cstdlib>

int main() {

    char *p = NULL;
    if ((p = getenv("OK"))) {
        printf("OK=%s\n", p);
    }
    return 0;
}
