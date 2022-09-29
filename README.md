# Python_C_Binding

### Updated 28 September 2022

## Primary Objective:
Trying to figure out how to write code in C and call it in Python to exploit the benefits and remove the drawbacks of both languages, with a little bit of over head.

__Status__: Complete

__Completion Date__: 26 September 2022

## Secondary Objective:
Produce as few files as possible when compiling C code into a .dll file for better file mangement and avoid a cluttered workspace.

__Status__: Complete

__Completion Date__: 26 September 2022

## Tertiary Objective:
Input values, specifically arrays, to .dll from Python and return values, specifically arrays, from .dll into Python

__Status__: In Progress

__Completion Date__:

## Lessons Learned

### 1. Create C code (CFILE.c) to be turned into dll
a. Write __declspec(dllexport) before any function to be called (FUNCTIONtobeCALLED()) by Python 

### 2. Compile C into a .dll file (DLLFILE.dll)
a. Run in command line or .bat file

    gcc -shared -o DLLFILE.dll CFILE.c

### 3. Write python file (PYFILE) that will use newly created dll
    import ctypes
    fname=".\DLLFILE.dll" # if in same directory else write file path r"C:\...
    dll = ctypes.CDLL(fname)
    dll.FUNCTIONtobeCALLED()

