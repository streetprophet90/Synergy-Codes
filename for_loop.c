#include <stdio.h>

int main(){

    // for(int i = 0; i < 10; i++) {
    //     printf("%d\n", i);
    // }


// Sum of all numbers from 1 to 100
    // int sum = 0;
    // for(int i = 1; i <= 100; i++) {
    // sum = sum + i;
    // }
    // printf("%d\n", sum);



// Sum of all even numbers between 1 and 100
    int sum = 0;
    for(int i = 2; i <= 100; i = i+2){
        sum = sum + 2;
    } 
    printf("%d\n", sum);

    return 0;
}