
import ctypes

fname=".\TestDll.dll"

dll = ctypes.CDLL(fname)

mult = dll.mult
mult.argtypes = [ctypes.c_float, ctypes.c_float]
mult.restype = ctypes.c_float

print("Py ", mult(2.5, 3.0))


