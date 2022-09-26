
gcc -c testcompiler.c -o test_dll.o
gcc -shared -o TestDll.dll -Wl,--out-implib,libtstdll.a test_dll.o