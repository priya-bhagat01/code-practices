//Program to find sum & avg of marks of 3 subjects
#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c,sum,avg;
clrscr();
printf("Enter First Marks: ");
scanf("%d",&a);
printf("Enter Second Marks: ");
scanf("%d",&b);
printf("Enter Third Marks: ");
scanf("%d",&c);
sum = a+b+c;
avg = sum/3.0;
printf("The Sum of three subjects is s %d",sum);
printf("\nThe Avg of three subjects is s %d",avg);
getch();
}