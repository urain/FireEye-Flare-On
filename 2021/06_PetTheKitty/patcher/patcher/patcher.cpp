#include <windows.h>
#include <iostream>

typedef int(__stdcall* f_ApplyDeltaA)(UINT64, LPCSTR, LPCSTR, LPCSTR);
typedef int(__stdcall* f_ApplyDeltaB)(UINT64, char *, char*, char*);

int main(int argc, char * argv[])
{
    HINSTANCE hGetProcIDDLL = LoadLibrary(L"msdelta.dll");

    // resolve function address here
    f_ApplyDeltaA ApplyDeltaA = (f_ApplyDeltaA)GetProcAddress(hGetProcIDDLL, "ApplyDeltaA");
    f_ApplyDeltaB ApplyDeltaB = (f_ApplyDeltaB)GetProcAddress(hGetProcIDDLL, "ApplyDeltaB");

    FILE* fptr;
    char patch0[4096];
    memset(patch0, 0, 4096);
    char buf[4096];
    memset(buf, 0, 4096);
    fopen_s(&fptr, "C:\\Users\\User\\Desktop\\patches\\0.pa30", "rb");
    fread(patch0, sizeof(buf), 1, fptr);
    std::cout << "funci() returned " << ApplyDeltaB(0, 0, patch0, buf) << std::endl;

    std::cout << "funci() returned " << ApplyDeltaA(0, argv[1], argv[2], argv[3]) << std::endl;

    return EXIT_SUCCESS;
}