#include <iostream>
using namespace std;

int main(){
    double xs[10] = {0.5, 2.5, 1, 2, 0.5, 1, 2, 1, 1.5, 2.5};
    double ys[10] = {4.5, 1.6, 3, 1.8, 5, 4.2, 2.4, 3.6, 3.3, 1.4};

    double slope = -1.5;
    double yint = 5.5;
    for(int i = 0; i < 10; i++){
        double nums = xs[i] * slope;
        cout << "Predicted: " << nums << endl;

        double r = nums - ys[i];
        cout << "Predicted: " << r << endl;
    }
}