#include <iostream>
#include <unordered_map>
using namespace std;
bool check_increasing(int num);
bool check_double(int num);
int arr[6];

int main()
{
    int start = 244444; //is there a way to do it with a stack?
    int stop = 784956;
    int count = 0;
    for(int i = start; i < stop; i ++){
        if(check_double(i) && check_increasing(i))
        {
            count++;
        }
    }
    cout << count << endl;
}
int * create_array(int num, int arr[6])
{
    int digit = num%10;
    for(int i = 5; i >= 0; i --)
    {
        arr[i] = digit;
        num = num/10;
        digit = num%10;
    }
    return arr;
}
bool check_double(int num)
{
    int * a;
    a = create_array(num, arr);
    unordered_map<int, int> map;
    for(int i = 1; i < 6; i ++)
    {
        if(arr[i] == arr[i-1])
        {
            std::unordered_map<int,int>::const_iterator got = map.find (arr[i]);

            if(got != map.end())  //contains
            {   
                int val = got->second + 1;

                map.erase(arr[i]);
                map.insert(std::make_pair(arr[i], val));
            }
            else
            {
                map.insert(std::make_pair(arr[i], 2));
            }
        }
    }
    bool contains = false;
    for (auto const &pair: map) {
        if(pair.second == 2)
        {
            contains = true;
        }
    }    
    return contains;
}

bool check_increasing(int num)
{
    int * a;
    a = create_array(num, arr);
    for(int i = 1; i < 6; i ++)
    {
        if(arr[i] < arr[i-1])
        {
            return false;
        }
    }
    return true;
}