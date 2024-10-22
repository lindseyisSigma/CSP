#include <stdio.h>
char sibs[3][20]= {" ana! ", " elsa! ", " olaf! "};
int i;
int main(){
    while(i<3){
        printf("%s", "Hello");
        printf("%s", sibs[i]);
        i++;
    }
    return 0;
}