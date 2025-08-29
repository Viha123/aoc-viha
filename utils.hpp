#pragma 
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
std::vector<std::vector<char>>
convert_input_into_char(std::vector<string> input);
std::vector<std::string> parse_file(const std::string &name);
template<typename T>
void print1d(const vector<T>& array) {
  for (int i = 0; i < array.size(); i++) {
    cout << array[i] << " " << endl;
  }
}
template<typename T>
void print2d(const vector<vector<T>>& array) {
  for (int i = 0; i < array.size(); i++) {
    for (int j = 0; j < array[0].size(); j++) {
      cout << array[i][j] << " ";
    }
    cout << endl;
  }
}

