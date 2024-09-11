#include <stdio.h>.h>

int main(void) {
    char favoriteSport[30];
    printf("What is your favorite sport: \n");
    fgets(favoriteSport, sizeof(favoriteSport), stdin);
    printf("Cool! \n");
    return 0;
}