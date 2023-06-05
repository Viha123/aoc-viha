#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include <stdlib.h>

void convert_to_vector(std::vector<int> &outputs, std::string content);
int main()
{
    std::fstream data("five.txt");
    std::string str;
    getline(data, str);
    std::cout << str << std::endl;

    
}
