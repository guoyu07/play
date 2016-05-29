// define a class for prime related oprations
#include <set>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;
struct PrimeBall {
    set<int> ps; // set used for storing primes
    void gen_primes(int upbond) {
        int* arr = (int*)malloc((upbond + 1) * sizeof(int));
        memset(arr, 0, (upbond + 1) * sizeof(int));
        int sieveup = (int)sqrt(upbond + 0.5);
        for (int i = 2; i <= sieveup; i++) {
            if (!arr[i]){
                for (int j = i * i; j <= upbond; j += i) arr[j] = 1;
            }
        }
        // after sieving, collect primes to set ps
        for (int i = 2; i <= upbond; i++) {
            if (arr[i] == 0) {
                ps.insert(i);
            }
        }
        free(arr);
    }
};

int main() {
    struct PrimeBall pb;
    pb.gen_primes(50);
    set<int>& tmp = pb.ps;
    set<int>::iterator it = tmp.begin();
    while (it != tmp.end()) {
        printf("%d\n", *it);
        it++;
    }
    return 0;
}
