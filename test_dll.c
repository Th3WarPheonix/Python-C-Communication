
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
__declspec(dllexport) int arrayC2(int lenrow, int lencol, double mat[lenrow][lencol]){
    int i, j;
    printf("C\n");
    for (i = 0; i<lenrow; i++){
        for (j = 0; i<lencol; j++){
            printf("%f ", mat[i][j]);
        }
        printf("%d", i);
        printf("\n");
        mat[i][j] = mat[i][j] + 1;
        }
    printf("\n");
    return 0;
}




