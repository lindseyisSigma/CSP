#include <stdio.h>

char sibs[3][20] = {"", "Alaiah", "Kaylee"};
int i;
int main (){
    for(i=0;i<3;i++)
    printf("%s Tabla\n", sibs[i]);
    return 0;
}