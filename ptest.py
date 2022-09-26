
import ctypes

fname=".\TestDll.dll"

dll = ctypes.OleDLL(fname)

dll.message()