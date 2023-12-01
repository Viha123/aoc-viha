#include <iostream>
#include <string>
#include <vector>
#include <fstream>
std::vector<std::string> parse_file(std::string name){
    std::ifstream myfile(name);
    std::string contents;
    std::vector<std::string> input;
    if(myfile.is_open()){
        while(myfile.good()){
            myfile >> contents;
            input.push_back(contents);
        }
    }
    return input;
}