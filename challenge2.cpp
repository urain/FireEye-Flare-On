// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <tchar.h>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <windows.h>
#include <Wincrypt.h>
#include <fstream>

#define PASSWORD_LENGTH 512

using namespace std;
int main()
{
	streampos size;
	char * memblock;
	ifstream myfile;
	BYTE *readin;
	readin = (BYTE *)malloc(4010);
	DWORD readinsize;
	myfile.open("C:\\Users\\User\\Desktop\\working\\challenge2\\BusinessPapers.doc", ios::in | ios::binary| ios::ate);
	if (myfile.is_open()) {
		size = myfile.tellg();
		memblock = new char[size];
		myfile.seekg(0, ios::beg);
		myfile.read(memblock, size);
		myfile.close();

		readinsize = size;
		cout << "the entire file content is in memory" << endl;
		readin = (BYTE *)malloc(size);
		for (int i = 0; i < size; i++) {
			readin[i] = (unsigned int)memblock[i];
			//printf("%c", (unsigned int)memblock[i]);
		}
	}
	//for (int i = 0; i < readinsize; i++) {
	//	printf("%02x ", readin[i]);
	//}


	myfile.close();

	HCRYPTPROV hCryptProv;
	HCRYPTKEY hKey;
	HCRYPTHASH hHash;
	CHAR szPassword[PASSWORD_LENGTH] = "thosefilesreallytiedthefoldertogether";
	DWORD dwLength;

	//----------------------------------------------------------------
	// Get the password from the user.
	dwLength = (DWORD)strlen(szPassword);

	//----------------------------------------------------------------
	// Acquire a cryptographic provider context handle.
	if (CryptAcquireContextW(
		&hCryptProv,	// 0x18ff6c == 0x4a9d80
		NULL,
		NULL,
		0x18,			// 0x18 == 24 == PROV_RSA_AES
		0))
	{
		printf("\nA context has been acquired. \n");
	}

	//----------------------------------------------------------------
	// Create an empty hash object
	if (CryptCreateHash(
		hCryptProv,		// 0x4a9d80 (original container)
		0x8004,			// CALG_SHA
		0,
		0,
		&hHash))		// 0x18faf8 == 0x4a9ad0  empty hash container
	{
		printf("An empty hash object has been created. \n");
	}

	//----------------------------------------------------------------
	// Hash the password string
	if (CryptHashData(
		hHash,				// 0x4a9ad0
		(BYTE *)szPassword,	// 0x4a9920
		dwLength,			// size of string
		0))
	{
		printf("The password has been hashed. \n");
	}

	//----------------------------------------------------------------
	// Create a session key based on the hash of the password.
	if (CryptDeriveKey(
		hCryptProv,		// 0x4a9d80 orig key container
		0x6610,			// CALG_AES_256
		hHash,			// 0x4a9ad0   SHA Hash container (DESTROYED)
		CRYPT_EXPORTABLE,
		&hKey))			// 0x18ff68 == 0x4a9b40   key
	{
		printf("The key has been derived. \n");
	}



	//------------
	// CryptSetKeyParam
	BYTE pbdata = 0x1;
	if (CryptSetKeyParam(
		hKey,			// 0x4a9b40   cryptderivekey
		0x4,			// KP_MODE
		(BYTE *)pbdata,	// 0x18fb1c == value of 0x1
		0)) 
	{
		printf("The Crypt Param Set.\n");
	}


	//--------------
	// CryptGetKeyParam
	BYTE *pbdata2;
	DWORD pbdata2len;
	pbdata2len = sizeof(DWORD);
	if (CryptGetKeyParam(
		hKey,				// 0x4a9b40		cryptderivekey
		0x8,				// KP_BLOCKLEN
		(BYTE *)&pbdata2,	// 0x18f278  ==  x80 == 128
		&pbdata2len,		// 0x18f26c	 ==  x04
		0))
	{
		printf("The Crypt Param has been Getted.\n");
	}



	// HEAP 2 = 0x59dca0

	//-------------
	HCRYPTHASH hHash2;
	if (CryptCreateHash(
		hCryptProv,	// 0x4a9d80 orig key container
		0x8003,		// CALG_MD5
		0,
		0,
		&hHash2))	// 0x18f27c = 0x4adcc8   new hash object
	{
	printf("A second hash object was created for md5. \n");
	}


	//----------------------------------------------------------------
	// Hash the file name.
	CHAR szFilename[PASSWORD_LENGTH] = "businesspapers.doc";
	DWORD dwLength2;
	dwLength2 = (DWORD)strlen(szFilename);

	if (CryptHashData(
		hHash2,				// 0x4adcc8 new md5 hash object
		(BYTE *)szFilename,	// 0x4adc78 filename 
		dwLength2,			// size of filename
		0))
	{
		printf("The filename has been hashed. \n");
	}

	//-------------
	BYTE *szMD5;
	szMD5 = (BYTE*)malloc(0x10);
	DWORD pbdata3len = 0x10;
	
	if (CryptGetHashParam(
		hHash2,				// 0x4adcc8   md5 hash of filename container (DESTROYED)
		0x2,				// HP_HASHVAL
		szMD5,				// 0x4adca0  MD5 hash of filename 03 4D 36 1A 59 42 E6 76 97 D1 75 34 F3 7E D5 A9
		&pbdata3len,		// 0x18f270 == 0x10
		0
		))
	{
		printf("\nGot hashval of md5'd filename\n");
	}

	for (int i = 0; i < pbdata3len; i++) {
		printf("%02x ", szMD5[i]);
	}

	//-------------------
	if (CryptSetKeyParam(
		hKey,			// 0x4a9b40   cryptderivekey
		0x1,			// probably KP_IV 
		szMD5,			// 0x4adca0  actual md5 of filename
		0))
	{
		printf("\nSetkeyparam KP_IV? Maybe to MD5 of filename\n");
	}


	//-------------
	BYTE *pbdata4;
	DWORD pbdata4len = 0x04;
	if (CryptGetKeyParam(
		hKey,				// 0x4a9b40 orig key
		0x8,				// KP_BLOCKLEN?
		(BYTE *)&pbdata4,	// 0x18f27c == 0x59dcc8
		&pbdata4len,		// 0x18f264 == 4
		0))
	{
		printf("CryptGetKeyParam for orig key\n");
		printf("BLOCKLEN = %i\n", pbdata4);
	}

	// heap 3 0x59f1d0
	//-----------------

	BYTE *pbBuffer = readin;
	DWORD textlen = readinsize;
	DWORD buffLen = textlen+16;

	cout << "READINSIZE: " << textlen << endl;

	/*for (int i = 0; i < textlen; i++) {
		printf("%02x ", pbBuffer[i]);
	}*/

	/*
	if (CryptEncrypt(
		hKey, //0x4a9b40 orig key
		0,
		0x1,
		0,
		pbBuffer,
		&textlen, //0x18f270
		buffLen))
	{
		printf("\nPerformed CryptEncrypt.\n");
	}*/

	//for (int i = 0; i < textlen; i++) {
	//	printf("%02x ", pbBuffer[i]);
	//}

	
	if (CryptDecrypt(hKey, 0, 0, 0, pbBuffer, &textlen)) {
		printf("\nPerformed CryptDecrypt.\n");
	}
	else {
		printf("\nERROR: %08x\n", GetLastError());
	}


 // end main

	ofstream f("C:\\Users\\User\\Desktop\\output.bin", ios::out | ios::app | ios::binary);
	//for (int i = 0; i < textlen; i++) {
		//printf("%c", pbBuffer[i]);
	//	f.write((const char *)pbBuffer, textlen);
	//}
	f.write((const char *)pbBuffer, textlen);
	f.close();
    return 0;
}

