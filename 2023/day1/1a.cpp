#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
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

std::vector<std::string> strings = {"two", "one", "three", "four", "five", "six", "seven", "eight", "nine"};
std::string numberfromstring(std::string fiveletterword)
{
    for (auto str : strings)
    {
        bool isFound = fiveletterword.find(str) != std::string::npos;
        if (isFound == 1)
        {
            // return substring
            return numbers[str];
        }
    }
    return "";
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
                else if(foundFirst == false)
                {
                    std::string word1 = contents.substr(i, 5);
                    std::string possible = numberfromstring(word1);
                    if (possible.length() != 0)
                    {
                        // found our number
                        foundFirst = true;
                        int n = std::stoi(possible);
                        char c = n + '0';
                        num[0] = c;
                    }
                }
                if (foundLast == false && isdigit(contents[last]))
                {
                    foundLast = true;
                    num[1] = contents[last];
                }

                else if(foundLast == false)
                {
                    std::string word1 = contents.substr(last, 5);
                    std::string possible = numberfromstring(word1);
                    if (possible.length() != 0)
                    {
                        // found our number
                        foundLast = true;
                        int n = std::stoi(possible);
                        char c = n + '0';
                        num[1] = c;
                    }
                }

                // if its not digit then we can try something else like taking next 5 letters and checking if it makes a word
                //

                i++;
                if (foundLast && foundFirst)
                {

                    std::cout << j+1 << " " << num << std::endl;
                    sum += atoi(num);
                    break;
                }
            }
            j++;
        }
    }

    std::cout << sum << std::endl;
    // std::string one = "1thsix";
    // std::string two = "six";
    // bool isFound = one.find(two) != std::string::npos;

    // std::cout << one.find(two) << std::endl;
}