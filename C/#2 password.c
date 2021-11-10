#include <stdio.h>
#include <string.h>

int main() { 
	// Password System
	char ans[50]="olahightierloot";
	char input[50];
	
	printf("Type your password: ");
	gets(input);
	// if..else method
	//if(strcmp(input,ans)==0)
	//{
	//	printf("\nHello Administrator\n");
	//}
	//else
	//{
	//	printf("\nWrong password\n");
	//}
	
	// While Method
	while(strcmp(input,ans)!=0)
	{
		printf("Wrong Password\n\nType your password: ");
		gets(input);
	}
	
	printf("\nHello Administrator\n");
	return 0;
}
