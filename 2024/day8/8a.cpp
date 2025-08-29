#include "../../utils.hpp"
#include <set>

#include <vector>
#include <ostream>
using namespace std;
int main() {
  // cout << "HERE " << endl;
  vector<string> input = parse_file("../sample.txt");
  vector<vector<char>> array = convert_input_into_char(input);
  set<pair<int,int>> antinodes;
  for (int i = 0; i < array.size(); i++) {
    for (int j = 0; j < array[0].size(); j++) {
      char current = array[i][j];
      if (current != '.') {
        // same column
        for (int r = 0; r < array.size(); r++) {
          if (array[r][j] == current && r != i) {
            // calculate
            pair<int, int> slopeLeft;
            slopeLeft.first = i - r;
            slopeLeft.second = 0; // same line the slope is 0
            if (antinodes.find(slopeLeft) == antinodes.end()) {
              antinodes.insert(slopeLeft);
            }
            pair<int, int> slopeRight;
            slopeRight.first = i + r;
            slopeRight.second = 0; // same line the slope is 0
            if (antinodes.find(slopeRight) == antinodes.end()) {
              antinodes.insert(slopeRight);
            }
          }
        }
        // same col
        // diagonal

      }   
    }
  }
  return 0;
  
}