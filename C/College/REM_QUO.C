//Program to compute Quotient & Remainder in division
#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,q,r;
clrscr();
printf("Enter First Number: ");
scanf("%d",&a);
printf("Enter Second Number: ");
scanf("%d",&b);
q = a/b;
r = a%b;
printf("The Quotient of two number is s %d",q);
printf("\n The Remainder of two number is s %d",r);
getch();
}