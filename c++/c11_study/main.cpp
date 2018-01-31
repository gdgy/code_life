#include <iostream>

using namespace std;

int s=101;

int&& foo(){return static_cast<int&&>(s);} //返回值为右值引用

int main() {
 int i=foo();   //右值引用作为右值，在赋值运算符的右侧
 int&& j=foo(); //j是具名引用。因此运算符左侧的右值引用作为左值
 int* p=&j;     //取得j的内存地址
}
