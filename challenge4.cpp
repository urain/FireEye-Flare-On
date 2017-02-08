f0ll0w_t3h_3xp0rts@flare-on.com

// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <Windows.h>
#include <algorithm>
#include <fstream>

using namespace std;


int main()
{
	HINSTANCE dllHandle = LoadLibrary(L"C:\\Users\\User\\Desktop\\flareon2016challenge.dll");
	DWORD base = (DWORD)dllHandle + 0x00007010;
	CHAR * encstring = (CHAR *)dllHandle + 0x00007014;
	int z = NULL;
	int ord = 30;
	char c = *encstring+0x13;

	while (ord <= 51) {
		FARPROC NumFunc = GetProcAddress((HMODULE)dllHandle, (LPCSTR)ord);
		if (NumFunc > 0) {
			int x = NumFunc();

			if (ord == 51) {
				break;
			}
			__asm {
				mov ord, eax // result of function
			}
		}

	}

	ord = 50;
	int beeprange[21][2] = { { 0x1f4,0x1b8 },{ 0x1f4, 0x1b8 },{ 0x1f4,0x1b8 },{ 0x15e,0x15d },{ 0x96,0x20b },{ 0x1f4,0x1b8 },{ 0x15e,0x15d },{ 0x96,0x20b },{ 0x3e8,0x1b8 },{ 0x1f4,0x293 },{ 0x1f4,0x293 },{0x1f4, 0x293}, { 0x15e,0x2ba },{ 0x96,0x20b },{ 0x1f4,0x19f },{ 0x15e,0x15d },{ 0x96,0x20b },{ 0x3e8,0x1b8 } };
	FARPROC NumFunc2 = GetProcAddress((HMODULE)dllHandle, (LPCSTR)ord);
	for (int o = 0; o <= 0x12; o++) {
		int a = beeprange[o][0];
		int b = beeprange[o][1];
		__asm {
			push a;
			push b;
		}
		int y = NumFunc2();
	}
	
	cout << "hh" << endl;
    return 0;
}

