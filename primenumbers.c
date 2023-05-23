#include <stdio.h>

//  a C code that checks if a given number is prime:

int isPrime(int num) {
    if (num <= 1) {
        return 0;  // Not prime
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0;  // Not prime
        }
    }

    return 1;  // Prime
}

int main() {
    int number;

    // Input the number
    printf("Enter a positive integer: ");
    scanf("%d", &number);

    // Check if the number is prime
    if (isPrime(number)) {
        printf("%d is a prime number.\n", number);
    } else {
        printf("%d is not a prime number.\n", number);
    }

    return 0;
}
