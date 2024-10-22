#include <stdio.h>
int i;
int main(){
    //loop that counts to 50
    for(i=0;i<=50;i++){
         //replace #'s divisible by 3 and 5 with "FizzBuzz"
         if(i%3==0 && i%5==0){
            printf("fizzbuzz\n");
         }else if (i%3==0){
            //replace #'s divisible by 3 with "Fizz"
            printf("fizz\n");
         }else if (i%5==0){
            //replace #'s divisible by 5 with "Buzz"
            printf("buzz\n");
         }else {
            //print the number
            printf("%d\n", i);
         }
    }

    return 0;
}