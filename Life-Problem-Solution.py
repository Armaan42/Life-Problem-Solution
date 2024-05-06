#include <iostream>
using namespace std;

int main() {
    cout << "DO YOU HAVE A PROBLEM IN LIFE ?" << endl;

    int choice;
    cout << "1. YES" << endl;
    cout << "2. NO" << endl;
    cout << "Enter the choice: ";
    cin >> choice;

    if (choice == 1) {
        cout << "CAN YOU DO SOMETHING ABOUT IT ?" << endl;

        int choice_1;
        cout << "1. YES" << endl;
        cout << "2. NO" << endl;
        cout << "Enter the choice: ";
        cin >> choice_1;

        if (choice_1 == 1) {
            cout << "THEN WHY WORRY?" << endl;
        }
        else if (choice_1 == 2) {
            cout << "THEN WHY WORRY?" << endl;
        }
    }
    else {
        cout << "THEN WHY WORRY?" << endl;
    }

    return 0;
}
