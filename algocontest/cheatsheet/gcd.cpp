#include <cstdio>

//欧几里得算法，也叫“辗转相除法”，计算最大公约数

template <typename T>

T gcd(T a, T b) {
    if (a == 0) return b;
    while (b != 0) {
        if (a > b) {
            a -= b;
        } else {
            b -= a;
        }
    }
    return a;
}

int main() {
    int a, b;
    while(scanf("%d%d", &a, &b) != EOF) {
        printf("%d\n", gcd(a, b));
    }
    return 0;
}
