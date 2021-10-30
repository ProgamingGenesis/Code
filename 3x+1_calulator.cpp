//updated for non-windows operation systems 
#include <iostream>
#include <time.h>
using namespace std;

void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

void odd_finder (int n){
    if(n % 2 == 0){
        n = n/2;
        cout << n << " ";
        delay(500);
        odd_finder(n);

    }
    else{
        n = n*3 + 1;
        delay(500);
        cout << n << " ";
        odd_finder(n);

        
    }
}
int main() {
    int n;
    cout << "\nPlease Press 'control-c' to stop code once loop has started (Doing this will close this window) \n \n";
    cout << "Enter an integer: ";
    cin >> n;

    odd_finder(n);



}
