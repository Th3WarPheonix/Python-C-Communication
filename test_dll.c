
#include <stdio.h>

// For checking basic functionality in Python
__declspec(dllexport) int message(){
    printf("Hello World from C\n");
    return 5;
}

// For checking input and return values in Python
__declspec(dllexport) float mult(float N, float N2){
    printf("C %f\n", N*N2);
    return N*N2;
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
__declspec(dllexport) int arrayC2(int numcol, int numrow, double mat[numrow][numcol]){
    int i, j;
    printf("%d, %d\n", numcol, numrow);
    printf("C\n");
    for (i = 0; i<numrow; i++){
        for (j = 0; j<numcol; j++){
            mat[i][j]++;
            printf("[%d, %d, %f] ", i, j, mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    return 0;
}

int Carray2(int numrow, int numcol, double mat[numrow][numcol]){
    for (int i = 0; i<numrow; i++){
        for (int j = 0; j<numcol; j++){
            printf("[%d, %d, %f] ", i, j, mat[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    return 0;
}

int Carray1(int numcol, int mat[numcol]){
    for (int i = 0; i<numcol; i++){
        printf("[%d, %d] ", i, mat[i]);
        }
    printf("\n");
    return 0;
}

// Confirming what functions can be called
int main(){
    printf("Hello World\n");

    int matrix1[5] = {4,6,7,8,9};
    size_t n = sizeof(matrix1)/sizeof(int);
    printf("size of m %d\n", n);
    Carray1(5, matrix1);

    size_t tn = sizeof(matrix1)/sizeof(int);
    printf("size of 2m %d\n", tn);
    printf("\n");

    double matrix2[2][5] = {{4.0, 6.0, 7.0, 8.0, 9.0}, {5.0, 10.0, 15.0, 20.0, 25.0}};
    size_t n2 = sizeof(matrix2)/sizeof(double);
    printf("size of m2 %d\n", n2);
    printf("%d\n", sizeof(matrix2));
    Carray2(5, 2, matrix2);

    size_t tn2 = sizeof(matrix2)/sizeof(double);
    printf("size of 2m2 %d\n", tn2);
    printf("%d %d\n", sizeof(matrix2), sizeof(double));

    return 0;
}




