#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <typeinfo>
#include <array>
#include <bits/stdc++.h>
#include <limits.h>
#include <stdlib.h>
#include <unordered_set>
#define N 3
class IntcodeComputer{
    public:
        IntcodeComputer(const std::vector<long long>& program){ //takes in the "program/code" can continue to be vector
            this->initial_program = program;
            this->program = program;
            relative_base = 0; //starts at 0

        }
        void reset(){
            program = initial_program; 
            complete = true;
            ip = 0;
            relative_base = 0;

        }
        int interpret(int ip, int param, int offset)
        {
            if(param == 0) //
            {
                return program[ip];
            }
            else if(param == 1)//position
            {
                return ip;
            }
            else{
                return relative_base+offset;
            }
            
        }
        long long compute()
        {    
            int mode = 0; //if mode = 0, then position mode, if mode = 1 then immediate mode
            long long output = -1;
            int input_ptr = 0;
            while(program[ip]!=99)
            {
                //program[ip] is a max 5 digit number which needs to be parsed to be 3 digit position par and 2 digit ip
                int op = program[ip]%100;
                long long x = program[ip];
                long long p1 = interpret(ip+1, (x/100)%10, program[ip+1]);
                long long p2 = interpret(ip+2, (x/1000)%10, program[ip+2]);
                long long p3 = interpret(ip+3, (x/10000)%10, program[ip+3]);
            
                if(op== 1){
                    program[p3] = program[p1] + program[p2];
                    ip+=4;
                }
                else if(op == 2){
                    program[p3] = program[p1] * program[p2];
                    ip+=4;
                }
                
                else if(op == 3)
                {
                    int inputPosition;
                    std::cin >> inputPosition;
                    program[p1] = inputPosition;
                    ip += 2;
                }
                else if(op==4){
                    output = program[p1]; //parameter
                    ip+=2;
                    std::cout << output << std::endl;
                }

                else if(op == 5){
                    if(program[p1]!= 0)
                    {
                        ip = program[p2];
                    }
                    else
                    {
                        ip+=3;
                    }
                }
                else if(op == 6)
                {
                    if(program[p1] == 0)
                    {
                        ip = program[p2];
                    }
                    else{
                        ip+=3;
                    }
                }
                else if(op == 7)
                {
                    program[p3] = program[p1] < program[p2];
                    ip+=4;
                }
                else if(op ==8)
                {
                    program[p3] = program[p1] == program[p2];
                    ip+=4;
                }
                else if(op == 9){
                    relative_base += program[p1];
                    ip+=2;
                }
            
            }
            complete = true;
            return output;
        }
        bool isComplete() {return complete;}
    private:
        std::vector<long long> program;
        std::vector<long long> initial_program;
        bool complete = false;
        int ip = 0;
        int relative_base;
};

void convert_to_vector(std::vector<long long> &outputs, std::string content)
{
    std::stringstream ss1(content);
    while (ss1.good())
    {
        std::string substr;
        std::getline(ss1, substr, ',');
        long long num = stoll(substr);
        outputs.push_back(num);
    }
}

int main()
{
    std::fstream data("nine.txt");
    std::string str;
    std::vector<long long> input; 
    std::getline(data, str);
    convert_to_vector(input, str);

    IntcodeComputer computer(input); 

    computer.compute();

}

