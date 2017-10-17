#include <iostream>
#include <thread>
using namespace std;

void foo()
{
  cout << "hello thread" << endl;
}

int main()
{
	thread t1(foo);
	t1.join();
}
