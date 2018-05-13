#include<stdio.h>
char buf2[200];

int main()[
    setvbuf(stdout,0,2,0);
    char buf[20];
    printf("what's your name: ");
    gets(buf);
    printf("leave message: ");
    gets(buf2);
    puts(buf2);

]