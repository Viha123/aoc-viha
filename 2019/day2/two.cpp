#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int computer(int array[],int size);
int main()
{
    vector<int> data{1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0};
    
    int size = data.size();

    int array[size] = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0};
    int temp[size];
    copy_n(array,size,temp);
    int output = computer(array,size); //output of 0,0
    //find value 1 and 2 if final answer needs to be 19690720
    int value = 19690720;
    int count = 0;
    int noun = 0;
    int verb = 0;
    for(int i = 0; i <= 99; i ++)
    {
        for(int j = 0; j <= 99; j++)
        {
            copy_n(temp, size, array);
            array[1] = i;
            array[2] = j;
            output = computer(array,size);
            if(output == value)
            {
                noun = i;
                verb = j;
                break;
            }
            count++;
        }
        
    }
    cout << 100 * noun + verb;
}
int computer(int array[],int size)
{    
    int opcode = 0; //+= 1 untill 99
    
    while(array[opcode]!=99)
    {
        // if(array[opcode+3]<size)
        // {
            if(array[opcode] == 1)
            {
                array[array[opcode+3]] = array[array[opcode+1]] + array[array[opcode+2]];
    
            }
            else if(array[opcode] == 2)
            {
                array[array[opcode+3]] = array[array[opcode+1]] * array[array[opcode+2]];
            }
            opcode+=4;
        // }
    
    }
    return array[0];
}