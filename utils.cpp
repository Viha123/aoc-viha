#include "utils.hpp"
using namespace std;
std::vector<std::string> parse_file(const std::string &name) {
  std::ifstream myfile(name);

  std::string contents;
  std::vector<std::string> input;
  if (myfile.is_open()) {

    while (myfile) {
      std::string myline;
      std::getline(myfile, myline);
      input.push_back(myline);
    }
  }
  input.pop_back();
  return input;
}

std::vector<std::vector<char>>
convert_input_into_char(std::vector<string> input) {
  std::vector<std::vector<char>> result;
  for (const auto &line : input) {
    std::vector<char> char_line(line.begin(), line.end());
    result.push_back(char_line);
  }
  return result;
}