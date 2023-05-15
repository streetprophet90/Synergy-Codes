#include <stdio.h>

int add_number(int num1, int num2);


int main(){
    

    int x = 3;
    int y = 4;
    int result = add_number(x, y);
    printf("%d", result);

    return 0;
}

   int add_number(int num1, int num2){
        int sum = num1 + num2;
        return sum;
    }


