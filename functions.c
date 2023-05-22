#include <stdio.h>

void greet() {
    printf("Good Morning\n");
}


// A function that Adds two integers but there is no return statement
/*
void squareNumber (int number){
    int square = number * number;
    printf("The square of %d is %d.\n", number, square);
}
*/

int addNumbers(int number1, int number2){
    int sum = number1 + number2;
    return sum;
}


int main(){

    int result = addNumbers(6, 7);
    printf("Result = %d\n", result);

    greet ();

    return 0;
}