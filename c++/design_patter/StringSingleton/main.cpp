#include <iostream>
#include "StringSingleton.h"
using namespace std;

int main()
{
    StringSingleton single = StringSingleton::Instance();
    cout << single.GetString() << endl;
    cout << "Hello world!" << endl;
    return 0;
}
