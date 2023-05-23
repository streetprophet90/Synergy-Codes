// Here's a C code that calculates the area of land for irrigation using Simpson's rule for numerical integration:

#include <stdio.h>
#include <math.h>

// Function to calculate the value of f(x)
double f(double x) {
    return /* Your function here */;
}

// Function to calculate the area using Simpson's rule
double calculateArea(double a, double b, int n) {
    double h = (b - a) / n;  // Step size
    double sum = f(a) + f(b);

    for (int i = 1; i < n; i += 2) {
        double x = a + i * h;
        sum += 4 * f(x);
    }

    for (int i = 2; i < n - 1; i += 2) {
        double x = a + i * h;
        sum += 2 * f(x);
    }

    return (h / 3) * sum;
}

int main() {
    double a, b;  // Limits of integration
    int n;        // Number of intervals

    // Input the limits of integration
    printf("Enter the lower limit: ");
    scanf("%lf", &a);
    printf("Enter the upper limit: ");
    scanf("%lf", &b);

    // Input the number of intervals
    printf("Enter the number of intervals (must be even): ");
    scanf("%d", &n);

    // Check if the number of intervals is even
    if (n % 2 != 0) {
        printf("Error: Number of intervals must be even.\n");
        return 1;
    }

    // Calculate the area using Simpson's rule
    double area = calculateArea(a, b, n);

    // Output the calculated area
    printf("The area of land for irrigation is: %.2lf\n", area);

    return 0;
}
