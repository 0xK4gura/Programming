#include <stdio.h>

int main(void) {
	// Adding value via operator
	unsigned char j = 200;
	j += 10;
	
	// Basic printf using stdio library
	printf("Hello, World!\n\n");
	printf("My name is k4gura, and I'm recently took an interest into programming and cybersecurity, I hope you can teach me more about it!\n\n");
	printf("Testing sum of number: %u \n\n", j);
	
	// Size of Variable Types ; variable need to always start with the type of variable we want to store
	printf("Char size: %lu \n", sizeof(char));
	printf("Long size: %lu \n", sizeof(long));
	printf("Long Double size: %lu \n", sizeof(long double));
	printf("Double size: %lu \n", sizeof(double));
	printf("Short size: %lu \n", sizeof(short));
	
	// Constant ; same as variable except need to prepend with 'const' ; its common to declare constant with uppercase
	const int age = 37;
	const int AGE = 12;
	#define AGES44 44
		
	printf("\n\nThe age of Abu, Ali and Amira are: %i, %i, %i\n\n\n", age, AGE, AGES44);

}
