#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>
#include <cstdio>
#include <array>
#include <algorithm>

#include <map>
#include "../../utils.cpp"
using namespace std;
#define RED 12
#define GREEN 13
#define BLUE 14
int day2(vector<string> input)
{
    int sum = 0; 
    for (auto line : input)
    {
        //find id of line
        int firstCp = line.find(" ");
        int secondCp = line.find(":");
        // string game_id = line.substr(line.find(" "), line.find(":"));
        cout << firstCp << " " << secondCp << endl;
    }
    return sum;
}
int main()
{
    vector<string> input = parse_file("two.txt");

    int sum = day2(input);

}