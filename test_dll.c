
#include <stdio.h>

// For checking basic functionality in Python
__declspec(dllexport) int message(){
    printf("Hello World 6\n");
    return 5;
}

// For checking input and return values in Python
__declspec(dllexport) float mult(float N, float N2){
    printf("C %f\n", N*N2);
    return N*N2;
}

// Confirming what functions can be called
int main(){
    printf("Hello World");
    return 0;
}

// For checking array input and output
__declspec(dllexport) int arrayC(int length1, double mat[length1]){
    int i;
    printf("C\n");
    for (i = 0; i<length1; i++){
        printf("%f ", mat[i]);
        mat[i] = mat[i] + 1;
        }
    printf("\n");
    return 0;
}

// For checking array input and output
__declspec(dllexport) int arrayC2(int lenrow, int lencol, double mat[lencol][lenrow]){
    int i, j;
    printf("%d, %d\n", lenrow, lencol);
    printf("C\n");
    for (i = 0; i<lencol; i++){
        for (j = 0; j<lenrow; j++){
            printf("[%d, %d, %f] ", i, j, mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    return 0;
}




