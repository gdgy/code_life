#define LEN 10
#include <iostream>
int len_foo() {
    return 5;
}

int main() {
    char arr_1[10];
    char arr_2[LEN];
    int len = 5;
    char arr_3[len];          // 非法
    const int len_2 = 10;
    char arr_4[len_2];        // 合法
    char arr_5[len_foo()+5];  // 非法
    int a;
    std::cout<< "input a:" ;
    std::cin >> a;
    char arr_6[a];
    std::cout << sizeof(arr_6);
    return 0;
}