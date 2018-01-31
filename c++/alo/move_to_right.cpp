#include <iostream>
#include <cstring>
using namespace std;

template<class T>
static int exchange(T&a, T&b)
{
    T t = a;
    a = b;
    b = t;
    return 0;
}

static int movetoright(char* array, int len)
{
    if (!array or len < 1 )
        return 0;
    int t = array[0];
    for(int i=1; i < len; ++i)
    {
        array[i-1] = array[i];
    }
    array[len-1] = t;
    return 0;
}

static int move_to_right_n(char* array, int len, int n)
{
    if (!array or len <  n)
        return 0;
    for(int i=0; i < len; ++i)
    {
        if (i+n < len)
            exchange(array[i], array[i+n]);
        else
            exchange(array[i], array[len-1]);
        if (i+n == len-1 && len%n == 0)
            break;
    }
    return 0;
}

static int move_to_right_n_end(char* array, int len, int n)
{
    if (!array or len <  n)
        return 0;
    int p1 = 0;
    int p2 = n;
    int k = len - n - len%n;
    while (k-- > 0)
    {
        exchange(array[p1++], array[p2++]);
    }
    int i = len - p2;
    while(i-- > 0)
    {
        int m = p2++;
        while(m > p1)
        {
            exchange(array[m-1], array[m]);
            --m;
        }
        p1++;
    }
}

int test()
{
    char array[] = "abcdefghijklmnopq";
    cout << array << endl;
    //movetoright(array, strlen(array));
    //movetoright(array, strlen(array));
    move_to_right_n_end(array, strlen(array), 2);
    cout << array << endl;
    return 0;
}
