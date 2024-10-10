#include <stdio.h>
char sibs[3][20] = {"Eric", "skibdi", "sigma"};
int i;
int main(){
    for(i=0;i<3;i++){
        printf("%s Lindsey\n", sibs(i));
    }
    return 0;
}