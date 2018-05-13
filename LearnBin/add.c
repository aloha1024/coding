#include<stdio.h>
int add(int x,int y)
{
    int result = x+y;
    return result;
}
int main()
{
    int a = 100;
    int b = 200;
    int c = add(a,b);
    return 0;
}
