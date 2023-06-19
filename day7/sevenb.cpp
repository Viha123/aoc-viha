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
class AmplifierProgram{
    public:
        AmplifierProgram(const std::vector<int>& program){ //takes in the "program/code" can continue to be vector
            this->initial_program = program;
            this->program = program;
        }
        void reset(){
            program = initial_program; 
            complete = true;
            ip = 0;
        }
        int interpret(int ip, int param)
        {
            if(param == 0)
            {
                return program[ip];
            }
            else
            {
                return ip;
            }
        }
        int compute(const std::vector<int> &input)
        {    
            int mode = 0; //if mode = 0, then position mode, if mode = 1 then immediate mode
            int output = -1;
            int input_ptr = 0;
            while(program[ip]!=99)
            {
                //program[ip] is a max 5 digit number which needs to be parsed to be 3 digit position par and 2 digit ip
                int op = program[ip]%100;
                int x = program[ip];
                int p1 = interpret(ip+1, (x/100)%10);
                int p2 = interpret(ip+2, (x/1000)%10);
                int p3 = interpret(ip+3, (x/10000)%10);
            
                if(op== 1){
                    program[p3] = program[p1] + program[p2];
                    ip+=4;
                }
                else if(op == 2)
                {
                
                    program[p3] = program[p1] * program[p2];
                    ip+=4;

                }
                
                else if(op == 3)
                {

                    program[p1] = input[input_ptr];
                    input_ptr+=1;
                    ip+=2;
                }
                else if(op==4)
                {
                    output = program[p1]; //parameter
                    ip+=2;
                    return output;
                }

                else if(op == 5)
                {
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
            
            }
            complete = true;
            return output;
        }
        bool isComplete() {return complete;}
    private:
        std::vector<int> program;
        std::vector<int> initial_program;
        bool complete = false;
        int ip = 0;
};

class IntcodeComputer{
    public:
        void addAmplifierProgram(const std::vector<int> &program){
            programs.emplace_back(program);
        }
        bool isLastComplete(){
            return programs.back().isComplete() == true;
        }
        int runAmplifierProgram(int index, const std::vector<int> &input){
            return programs[index].compute(input);
        }
        void resetAmplifierProgram(int index){
            programs[index].reset();
        }
        bool isComplete(int index){
            return programs[index].isComplete();
        }
        void reset(){
            programs.clear();
        }

    private:
        std::vector<AmplifierProgram> programs; 
};

//gonna have 5! different non repeating  combinations. need to use dfs/backtracking to sovle problem
void dfs(std::unordered_set<int> hset, std::vector<std::vector<int>>& combinations,std::vector<int> vec){
    //base case
    if(hset.size() == 0){
        //append vector to combinations
        combinations.push_back(vec);
        return;
    }
    for(auto element: hset){
        std::vector<int> v2 = vec;
        std::unordered_set<int> set2 = hset;
        v2.push_back(element);
        set2.erase(element);
        dfs(set2,combinations,v2);
    }
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
int test_amplifier_configuration(IntcodeComputer& computer,const std::vector<int> &program ,const std::vector<int>& phase_setting){
    
    int output = 0; 
    int valid = 0;
    for(int i = 0; i < phase_setting.size(); i ++){
        computer.addAmplifierProgram(program);
    }//adding all the 5 programs into the computer, so that every program can maintain its own state.

    for(int i = 0; i < phase_setting.size(); i ++){
        output = computer.runAmplifierProgram(i, {phase_setting[i],output});
    }
    while(!computer.isLastComplete()){
        for(int i = 0; i < phase_setting.size(); i ++){
            output = computer.runAmplifierProgram(i, {output}); //after the first one, no need to send phase settings
            if(output!=-1){
                valid = output;
            }
        }
    }

    computer.reset();
    return valid;
}
int main()
{
    std::fstream data("seven.txt");
    std::string str;
    std::vector<int> input; 
    std::getline(data, str);
    convert_to_vector(input, str);

    std::unordered_set<int> hset = {5,6,7,8,9}; //this will be passed into every dfs func
    std::vector<std::vector<int>> combinations;
    std::vector<int> vec; //this will be appended into combinations 
    dfs(hset, combinations,vec); 
    int max = INT_MIN;
    IntcodeComputer computer; 
    
    // for(int i = 0; i < hset.size(); i ++){
    //     AmplifierProgram program(input);
    //     computer.addAmplifierProgram(program);
    // }
    for(auto outer: combinations){
    
        int initial = test_amplifier_configuration(computer, input, outer);
        if(initial > max){
            max = initial;
        }
    }
    std::cout<< max << std::endl;


    
}

