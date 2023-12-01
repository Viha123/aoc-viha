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
int interpret(int ip, int param, int array[]);
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
    int ip = 0; //+= 1 untill 99
    int mode = 0; //if mode = 0, then position mode, if mode = 1 then immediate mode
    
    while(array[ip]!=99)
    {
        //array[ip] is a max 5 digit number which needs to be parsed to be 3 digit position par and 2 digit ip
        int op = array[ip]%100;
        int x = array[ip];
        int p1 = interpret(ip+1, (x/100)%10, array);
        int p2 = interpret(ip+2, (x/1000)%10, array);
        int p3 = interpret(ip+3, (x/10000)%10, array);
    
        if(op== 1)
        {
            
            array[p3] = array[p1] + array[p2];
            ip+=4;

        }
        else if(op == 2)
        {
           
            array[p3] = array[p1] * array[p2];
            ip+=4;

        }
        
        else if(op == 3)
        {
            int inputPosition;
            std::cin >> inputPosition;
            array[p1] = inputPosition;
            ip += 2;
        }
        else if(op==4)
        {
            int output = array[p1]; //parameter
            std::cout << output << std::endl;
            ip+=2;
        }

        else if(op == 5)
        {
            if(array[p1]!= 0)
            {
                ip = array[p2];
            }
            else
            {
                ip+=3;
            }
        }
        else if(op == 6)
        {
            if(array[p1] == 0)
            {
                ip = array[p2];
            }
            else{
                ip+=3;
            }
        }
        else if(op == 7)
        {
            
            
            array[p3] = array[p1] < array[p2];
            ip+=4;
        }
        else if(op ==8)
        {
            
            array[p3] = array[p1] == array[p2];
            ip+=4;
        }
    
    }
    
}
int interpret(int ip, int param, int array[])
{
    if(param == 0)
    {
        return array[ip];
    }
    else
    {
        return ip;
    }
}