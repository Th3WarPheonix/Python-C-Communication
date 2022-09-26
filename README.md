# Python_C_Binding

### Updated 26 September 2022

## Primary Objective:
Trying to figure out how to write code in C and call it in Python to exploit the benefits and remove the drawbacks of both languages, with a little bit of over head.
### Status:
Complete
### Completion Date:
26 September 2022

## Secondary Objective:
Produce as few files as possible when compiling C code into a .dll file for better file mangement and avoid a cluttered workspace.
### Status:
In Progress
### Completion Date:
26 September 2022

## Final Notes
Steps for creating dll in C then executed in Python

1. Create C code (CFILE.c) to be turned into dll
    a. Write __declspec(dllexport) before any function to be called (FUNCTIONtobeCALLED()) by Python 

2. Compile C into a .dll file (DLLFILE.dll)
    a. Run in command line or .bat file
        gcc -shared -o DLLFILE.dll CFILE.c

3. Write python file (PYFILE) that will use newly created dll
    import ctypes
    fname=".\DLLFILE.dll" # if in same directory else write file path r/...
    dll = ctypes.CDLL(fname)
    dll.FUNCTIONtobeCALLED()

