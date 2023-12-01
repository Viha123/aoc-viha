#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <array>
#include <algorithm>

#include <map>
std::map<std::string, std::string> numbers = {
    {"two", "2"},
    {"one", "1"},
    {"three", "3"},
    {"four", "4"},
    {"five", "5"},
    {"six", "6"},
    {"seven", "7"},
    {"eight", "8"},
    {"nine", "9"}};

std::vector<std::string> strings = {"eight", "two", "one", "three", "four", "five", "six", "seven", "nine"};


char numberfromstring(std::string fiveletterword)
{
    for (auto str : strings)
    {
        
        if (fiveletterword.find(str) != std::string::npos){ //only detect if its found on the first string
            int index = fiveletterword.find(str);
            if(index == 0){
                int n = std::stoi(numbers[str]);
                char c = n + '0';
                return c;
            }
        }
    }
    return '0';
}


int main()
{
    // parse string first letter needs to
    std::ifstream myFile("1a.txt");
    std::string contents;

    int sum = 0;
    if (myFile.is_open())
    {
        int j = 0;
        while (myFile.good())
        {
            myFile >> contents;
            bool foundFirst = false;
            bool foundLast = false;
            int i = 0;
            char num[2] = {0};
            while (i < contents.length())
            {
                int last = contents.length() - i - 1;
                if (foundFirst == false && isdigit(contents[i]))
                {
                    foundFirst = true;
                    num[0] = contents[i];
                }
                else if (foundFirst == false)
                {
                    std::string word1 = contents.substr(i, 5);
                    char possible = numberfromstring(word1);
                    if (possible != '0')
                    {
                        // found our number
                        foundFirst = true;
                        num[0] = possible;
                    }
                }
                if (foundLast == false && isdigit(contents[last]))
                {
                    foundLast = true;
                    num[1] = contents[last];
                }

                else if (foundLast == false)
                {
                    std::string word1 = contents.substr(last, 5);
                    char possible = numberfromstring(word1);
                    if (possible != '0')
                    {
                        // found our number
                        foundLast = true;
                        num[1] = possible;
                    }

                }
                i++;
                if (foundLast && foundFirst)
                {
                    std::cout << j + 1 << " " << num << " " << std::endl;
                    sum += atoi(num);
                    break;
                }
            }
            j++;
        }
    }

    std::cout << sum << std::endl;

}