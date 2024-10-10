#include <stdio.h>
#include <string.h>
int i;
int usr;
char one[50];
char two[50];
char three[49];
int main(void){
    printf("Give me a number ");
    scanf("%d", &usr);
    printf("Give me a short word!\n");
    scanf("%s", &one);
    printf("Give me a short word!\n");
    scanf("%s", &two);
    strcar(three, one);
    strcat(three, two);
    //loop that counts to 50
    for(i=1;i<=usr;i++){

        //replace #'s diisible by 3 and 5 with "FizzBuzz"
         if(i%3==0 && i%5==0){
            printf("%s\n", three);
        
        //replace #'s divisible by 3 with "Fizz"
            printf("%s\n", two);
         } else if (i%5==0){
        //replace #'s dividible bt 5 with "Buzz"
            printf("Buzz\n");
         }else {
        //print the number
            printf("%d\n",i);
         }
    }
}