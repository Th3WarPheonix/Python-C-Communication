
#include <stdio.h>

__declspec(dllexport) int message(){
    printf("Hello World 6\n");
    return 5;
}

__declspec(dllexport) float mult(float N, float N2){
    printf("C %f\n", N*N2);
    return N*N2;
}

int main(){
    printf("Hello World");
    return 0;
}





