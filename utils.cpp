#include <iostream>
#include <string>
#include <vector>
#include <fstream>
std::vector<std::string> parse_file(std::string name)
{
    std::ifstream myfile(name);
    std::string contents;
    std::vector<std::string> input;
    if (myfile.is_open())
    {
        
        while (myfile)
        {
            std::string myline;
            std::getline(myfile, myline);
            input.push_back(myline);
        }
    }
    return input;
}