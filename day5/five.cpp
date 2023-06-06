#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <typeinfo>
#include <array>
#include <bits/stdc++.h>
#include <limits.h>
#include <stdlib.h>

void convert_to_vector(std::vector<int> &outputs, std::string content);
int interpret(int opcode, int param, int array[]);
void computer(int array[],int size);
int main()
{
    std::fstream data("five.txt");
    std::string str;
    std::vector<int> input; 
    std::getline(data, str);
    convert_to_vector(input, str);
    int size = input.size();
    int code[size];
    for(int i = 0; i < size; i ++)
    {
        code[i] = input.at(i);
    }

    computer(code, size);
    
}

void convert_to_vector(std::vector<int> &outputs, std::string content)
{
    std::stringstream ss1(content);
    while (ss1.good())
    {
        std::string substr;
        std::getline(ss1, substr, ',');
        int num = stoi(substr);
        outputs.push_back(num);
    }
}
void computer(int array[],int size)
{    
    int opcode = 0; //+= 1 untill 99
    int mode = 0; //if mode = 0, then position mode, if mode = 1 then immediate mode
    
    while(array[opcode]!=99)
    {
        //array[opcode] is a max 5 digit number which needs to be parsed to be 3 digit position par and 2 digit opcode
        int op = array[opcode]%100;
        int params = array[opcode]/100;
        int param1 = params%10;
        int param2 = (params/10)%10;
        int param3 = (params/100);
    
        if(op== 1)
        {
            if(param3 ==0)
            {
                array[array[opcode+3]] = interpret(opcode+1, param1, array) + interpret(opcode+2, param2, array);
            
            }
            else{
                array[opcode+3] = interpret(opcode+1, param1, array) + interpret(opcode+2, param2, array);
            }

            opcode+=4;

        }
        else if(op == 2)
        {
            if(param3 ==0)
            {
                array[array[opcode+3]] = interpret(opcode+1, param1, array) * interpret(opcode+2, param2, array);
            
            }
            else{
                array[opcode+3] = interpret(opcode+1, param1, array) * interpret(opcode+2, param2, array);
            }

            opcode+=4;

        }
        
        else if(op == 3)
        {
            int inputPosition;
            std::cin >> inputPosition;
            if(param1==0)
            {
                array[array[opcode+1]] = inputPosition;

            }
            else{
                array[opcode+1] = inputPosition;
            }
            opcode += 2;
        }
        else if(op==4)
        {
            int output = interpret(opcode+1, param1, array); //parameter
            std::cout << output << std::endl;
            opcode+=2;
        }
    
    }
    
}
int interpret(int opcode, int param, int array[])
{
    if(param == 0)
    {
        return array[array[opcode]];
    }
    else
    {
        return array[opcode];
    }
}