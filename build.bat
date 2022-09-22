
gcc -c test_dll.c
gcc -shared -o TestDll.dll -Wl,--out-implib,libtstdll.a test_dll.o