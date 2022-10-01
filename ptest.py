
import ctypes
import numpy as np

fname=".\TestDll.dll"
dll = ctypes.CDLL(fname)

print('_________Variable Types_________')
# Priming function call with appropriate types specified in C file
mult = dll.mult
mult.argtypes = [ctypes.c_float, ctypes.c_float]
mult.restype = ctypes.c_float # default is c_int

print("Py ", mult(2.5, 3.0))

print('_________Declare C arrays in Python________')
# How C arrays are treated in Python
array = ctypes.c_int*10 # array is now an array that acts a C array and must be printed one element at a time
print(array) # not normal array output because it is a C array
for i in array(5): print(i, end=' ')
print()
for i in array(4): print(i, end=' ')
print()
for i in array(5,4,3,2,1,6,7,8,9,0): print(i, end=' ')
print()

print('_________compatibility with numpy arrays________')
N = 7
array_values = np.linspace(7, 7+N, N+1)
array2 = ctypes.c_double*len(array_values)
print(array_values)
print(array2)

print('_________Passing arrays_________')
#Priming the function
arrayc = dll.arrayC 
arrayc.argtypes = [ctypes.c_int, ctypes.c_double*len(array_values)]
arrayc.restype = ctypes.c_int

array3 = array2(*array_values) # Make sure array2 ctype is same type as array_values when combining
print('Python values')
for i in array3: print(i, end=' ')
print()
arrayc(N+1, array3)

print('_________Summary of declaring 1D arrays_________')
N = 7
values = np.linspace(10, 10+N, N+1)
carray = ctypes.c_double*len(values) # c_type must match numpy array value type
varray = carray(*values)
print(values)
print(carray)
print(varray)
for i in varray: print(i, end=' ')
print()

N = 4
values2 = np.array(np.linspace(2, 3, N))
carray2 = ctypes.c_double*len(values2) # c_type must match numpy array value type
varray2 = carray2(*values2)
print(values2)
print(carray2)
print(varray2)
for i in varray2: print(i, end=' ')
print()

print('_________Passing 2d arrays_________')
N1 = 8
N2 = 2
values3 = np.array([np.linspace(1, 5, N1), np.linspace(20, 25, N1)])
carray3 = ctypes.c_double*values3.shape[0] # c_type must match numpy array value type
varray3 = np.ctypeslib.as_ctypes(values3)
print(values3)
print(carray3)
print(varray3)

print('Python')
for i in varray3:
    for j in i:
        print(j, end=' ')
    print()
print()

# Priming function
arrayC2 = dll.arrayC2
arrayC2.argtypes = [ctypes.c_int, ctypes.c_int, (ctypes.c_double*values3.shape[1])*values3.shape[0]]
arrayC2.restype = ctypes.c_int
arrayC2(N1, N2, varray3)

print(values3[0][5])


