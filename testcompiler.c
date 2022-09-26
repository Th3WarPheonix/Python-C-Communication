
#include <stdio.h>
#include "test_dll.h"

int main(){
    printf("Hello World");
    return 0;
}

EXPORT void message(){
    printf("Hello World dll");
}