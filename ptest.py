
import ctypes
import numpy as np

fname=".\TestDll.dll"
dll = ctypes.CDLL(fname)

# Priming function call with appropriate types specified in C file
mult = dll.mult
mult.argtypes = [ctypes.c_float, ctypes.c_float]
mult.restype = ctypes.c_float # default is c_int

print("Py ", mult(2.5, 3.0))

# How C arrays are treated in Python
array = ctypes.c_int*10 # array is now an array that acts a C array and must be printed one element at a time
print(array) # not normal array output because it is a C array
for i in array(5): print(i, end=' ')
print()
for i in array(4): print(i, end=' ')
print()
for i in array(5,4,3,2,1,6,7,8,9,0): print(i, end=' ')
print()

# Checking compatibility with numpy arrays
N = 7
array_values = np.linspace(7, 7+N, N+1)
print(array_values)
array2 =  ctypes.c_double*len(array_values)
print(array2)

# How to handle passing in arrays to C
# Make sure array2 ctype is same type as array_values
for i in array2(*array_values): print(i, end=' ')
print()
# Priming function
arrayc = dll.arrayC
arrayc.argtypes = [ctypes.c_int, ctypes.c_double*len(array_values)]
arrayc.restype = ctypes.c_int

array3 = array2(*array_values)
arrayc(N+1, array3)
for i in array3: print(i, end=' ')
print()

# Passing in 2D arrays
array_values = np.array([np.linspace(0,2,3), np.linspace(0,2,3)])
print(array_values)
print(array_values.shape)
for i in range(array_values.shape[0]):
    for j in range(array_values.shape[1]):
        print(array_values[i][j])
# Priming function
arrayc2 = dll.arrayC2
arrayc2.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_double*array_values.shape[0]*array_values.shape[1]]
arrayc2.restype = ctypes.c_int


