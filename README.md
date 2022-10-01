# Python_C_Binding

### Updated 01 October 2022

## Primary Objective:
Trying to figure out how to write code in C and call it in Python to exploit the benefits and remove the drawbacks of both languages, with a little bit of over head.

__Status__: Complete

__Completion Date__: 26 September 2022

## Secondary Objective:
Produce as few files as possible when compiling C code into a .dll file for better file mangement and avoid a cluttered workspace.

__Status__: Complete

__Completion Date__: 26 September 2022

## Tertiary Objective:
Input values and arrays, 1D and 2D, to dll from Python and return them from dll into Python

__Status__: In Progress

__Completion Date__: 01 October 2022

## How to Replicate Objectives

### 1. Create C code (cfilename.c) to be turned into dll
a. Write __declspec(dllexport) before any function to be called by Python

    __declspec(dllexport) int HelloWorld(){
        printf("Hello Python World from C\n");
        return 0;
    }

### 2. Compile C into a .dll file (dllfilename.dll)
a. Run in command line or .bat file

    gcc -shared -o dllfilename.dll cfilename.c

### 3. Write python file that will use newly created dll
    import ctypes
    import numpy as np

    fname=".\dllfilename.dll" # if in same directory else write file path r"C:\...
    dllfile = ctypes.CDLL(fname)
    dllfile.HelloWorld()

### 4. Pass 2D Array from Python to DLL
C code that prints out the matrix passed to it from Python. If the C code is changed it must be recompiled into dll using step 2 for the changes to be used in Python.

        __declspec(dllexport) int CArray(int numcol, int numrow, double mat[numrow][numcol]){
        for (int i = 0; i<numrow; i++){
            for (int j = 0; j<numcol; j++){
                printf("[%d, %d, %f] ", i, j, mat[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        return 0; /* The array is passed by reference so it does not have to be returned and can be called in Python with new values if the C function changes the array's values */
    }

Python code that passes array to dll

    N1, N2 = 8, 2
    nparray = np.array([np.linspace(1, 5, N1), np.linspace(20, 25, N1)]) # Creating numpy array because that's the most common way to make arrays
    cnparray = np.ctypeslib.as_ctypes(nparray) # Built in numpy functin that converts its types to ctypes types

    arrayC = dllfile.CArray
    arrayC.argtypes = [ctypes.c_int, ctypes.c_int, (ctypes.c_double*nparray.shape[1])*nparray.shape[0]] # Specifying argument types that match the C funcion argument types
    arrayC.restype = ctypes.c_int # Specifying return type that matches the C funcion return types

    arrayC(N1, N2, cnparray) # Calling dll function

    print(cnparray[0][0]) # Confirming the values are in the right position and are changed appropriately if above C code is changed





