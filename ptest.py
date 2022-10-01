
import ctypes
import numpy as np

fname=".\TestDll.dll"
dll = ctypes.CDLL(fname)

def printarray(array):
    """For printing ctype arrays of 1-2 dimensions"""

    try:
        for i in array:
            for j in i:
                print(j, end=' ')
            print()
        print()
    except:
        for i in array:
            print(i, end=' ')
        print()
        

def CtypeVariables():
    """Experimenting with ctypes types and how they work with the C code"""
    print('\nVARIABLE TYPES')

    # Priming function call with appropriate types specified in C file
    mult = dll.mult
    mult.argtypes = [ctypes.c_float, ctypes.c_float]
    mult.restype = ctypes.c_float # default is c_int
    print("Py ", mult(2.5, 3.0))

def CtypeArrays():
    """How to declare arrays in ctypes and print out their elements"""
    print('\nDECLARING CTYPE ARRAYS')

    array = ctypes.c_int*10 # array is now an array that acts a C array and must be printed one element at a time
    print(array) # not normal array output because it is a C array
    for i in array(5): print(i, end=' ')
    print()
    for i in array(4): print(i, end=' ')
    print()
    for i in array(5,4,3,2,1,6,7,8,9,0): print(i, end=' ')
    print()
    printarray(array(10, 5, 6, 9, 8, 55, 99, 101, 555, 678))

def CtypeArraysfromnparrays():
    """How to change a numpy array to a ctype array"""
    print('\nNUMPY ARRAYS TO CTYPE ARRAYS')

    N = 7
    array_values = np.linspace(7, 7+N, N+1)
    array2 = ctypes.c_double*len(array_values)
    print(array_values)
    print(array2)
    array3 = np.ctypeslib.as_ctypes(array_values)
    printarray(array3)

def Pass1DArraystoDLL():
    """How to pass 1D array to DLL"""
    print('\n1D ARRAYS TO DLL')

    N = 7
    array_values = np.linspace(7, 7+N, N)
    array2 = ctypes.c_double*len(array_values)
    array3 = array2(*array_values) # Make sure array2 ctype is same type as array_values when combining

    #Priming the function
    arrayc = dll.arrayC 
    arrayc.argtypes = [ctypes.c_int, ctypes.c_double*len(array_values)]
    arrayc.restype = ctypes.c_int

    print('Python values')
    printarray(array3)

    arrayc(N, array3)
    print('np array')
    arrayc(N, np.ctypeslib.as_ctypes(array_values))

def Declaring1DCtypeArrays():
    """Summary of delcaring 1D ctypes arrays"""
    print('\nSUMMARY OF DECLARING 1D ARRAYS')

    N = 7
    values = np.linspace(10, 10+N, N+1)
    carray = ctypes.c_double*len(values) # c_type must match numpy array value type
    varray = carray(*values)
    print(values)
    print(carray)
    print(varray)
    printarray(varray)

    N = 4
    values2 = np.array(np.linspace(2, 3, N))
    carray2 = ctypes.c_double*len(values2) # c_type must match numpy array value type
    varray2 = carray2(*values2)
    print(values2)
    print(carray2)
    print(varray2)
    printarray(varray2)

def Passing2DArraystoDLL():
    """How to declare and pass 2D ctype arrays"""
    print('\nPASSING 2D ARRAYS')

    N1 = 8
    N2 = 2
    values3 = np.array([np.linspace(1, 5, N1), np.linspace(20, 25, N1)])
    carray3 = ctypes.c_double*values3.shape[0] # c_type must match numpy array value type
    varray3 = np.ctypeslib.as_ctypes(values3)
    print(values3)
    print(carray3)
    print(varray3)

    print('Python')
    printarray(varray3)

    # Priming function
    arrayC2 = dll.arrayC2
    arrayC2.argtypes = [ctypes.c_int, ctypes.c_int, (ctypes.c_double*values3.shape[1])*values3.shape[0]]
    arrayC2.restype = ctypes.c_int
    arrayC2(N1, N2, varray3)

    print(values3[0][5])


if __name__ == '__main__':
    CtypeVariables()
    CtypeArrays()
    CtypeArraysfromnparrays()
    Pass1DArraystoDLL()
    Declaring1DCtypeArrays()
    Passing2DArraystoDLL()


