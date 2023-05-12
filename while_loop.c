#include <stdio.h>

int main(){

// This creates an infinite while loop. The code is executed until the memory runs out. 
    // while (1<5) {
    //     printf("While loop in C");
    // }



// This terminates the loop when the condition becomes false
    /*
    int count = 1;

    while (count < 5) {
        printf("While loop in C\n");
        printf("Count = %d\n", count);
        count = count + 1;
    }
    */



// This create a Multiplication Table
/*
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);

    int count = 1;

    while (count <= 10) {
        int product = number * count;
        printf("%d*%d = %d\n", number, count, product);
        count = count + 1;
    }
    */


    //DO WHILE LOOP
    
    int count = 1;
    do {
        printf("%d\n", count);
    } while (count < 5);
    count = count + 1;


    return 0;
}

