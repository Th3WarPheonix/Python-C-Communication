
import ctypes

fname=".\TestDll.dll"

dll = ctypes.CDLL(fname)

dll.message()