#include <pthread.h>
#include <stdio.h>


void* thread_entry(void* arg) {
    pthread_t tid = pthread_self();
    pthread_detach(tid);
    // did nothing just printing
    printf("hello thread!\n");
    
    char* val = "HELLO";

    pthread_exit(val); 
}

int main() {
    pthread_t tid;

    int ret = pthread_create(&tid, NULL, &thread_entry, NULL);
    
    void *val = NULL;

    pthread_join(tid, &val);
    
    printf("join out: %s\n", (char*)val);

    if (ret == 0) {
        printf("thread created successfully!\n");
    } else {
        printf("thread created failed with code %d returned.\n", ret);
    }
    
    return 0;
}
