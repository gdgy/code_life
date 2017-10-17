/*************************************************************************
    > File Name: test_init_struct.c
    > Created Time: Mon 18 Sep 2017 11:32:09 AM CST
 ************************************************************************/

#include<stdio.h>
typedef struct{
int a;
char b;
} test_struct;

int main()
{
	test_struct tmp = {5, 'a'};
	printf("%d\n", tmp.a);
	//tmp = {6, '4'};
}
