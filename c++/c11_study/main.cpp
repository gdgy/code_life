#include <iostream>

using namespace std;

int s=101;

int&& foo(){return static_cast<int&&>(s);} //����ֵΪ��ֵ����

int main() {
 int i=foo();   //��ֵ������Ϊ��ֵ���ڸ�ֵ��������Ҳ�
 int&& j=foo(); //j�Ǿ������á���������������ֵ������Ϊ��ֵ
 int* p=&j;     //ȡ��j���ڴ��ַ
}
