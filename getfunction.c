#include <stdio.h>

int main() {
    int birthYear, currentYear, age;
    
    // Input the birth year
    printf("Enter the birth year: ");
    scanf("%d", &birthYear);
    
    // Input the current year
    printf("Enter the current year: ");
    scanf("%d", &currentYear);
    
    // Calculate the age
    age = currentYear - birthYear;
    
    // Output the age
    printf("The age of a sixteen-year-old in %d is: %d\n", currentYear, age);
    
    return 0;
}
