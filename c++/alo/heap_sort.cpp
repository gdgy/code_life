#include <iostream>
#include <cstring>
#include <cstdlib>

static void swap(int& a, int& b){
    int tmp = b;
    b = a;
    a = tmp;
}

static void output(int *array, int len)
{
    for (int i = 1; i != len; ++i)
        std::cout << array[i] << " ";
    std::cout << std::endl;
}

static void swim(int * array, int insert_loc){
    int parent = insert_loc/2;
    if (array[parent] > array[insert_loc] && parent > 0){
        swap(array[parent], array[insert_loc]);
        swim(array, parent);
    }
    output(array, 10);
}

static int min_loc(int* array, int parent, int right, int left, int len)
{
    int loc = parent;
    if (array[loc] > array[right] && right < len)
        loc = right;
    if (array[loc] > array[left] && left < len)
        loc = left;
    return loc;
}

static void sink(int * array, int k, int len){
    int left = 2*k;
    int right = 2*k + 1;
    int loc = min_loc(array, k, right, left, len);
    if (loc != k){
        swap(array[k], array[loc]);
        sink(array, loc, len);
    }
    //output(array, 10);
}



int test()
{
    int array[10];
    memset(array, 0x00, sizeof(array)/sizeof(array));
    output(array, 10);
    for(int i=1; i != 10; ++i)
    {
        array[i] = 10 - i;
        swim(array, i);
    }
    
    for (int i = 0; i != 10; ++i)
        std::cout << array[i] << " ";
    std::cout << std::endl;
    for (int i = 1; i != 10; ++i){
        std::cout << array[1] << " ";
        array[1] = array[10 -i];
        array[10 -i] = 0;
        sink(array, 1, 10-i);
    }
    std::cout << std::endl;
}

int main()
{
    
    test();
}