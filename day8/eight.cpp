#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <stdlib.h>
#include <bits/stdc++.h>

using namespace std;
int main(){
    vector<int> image_data;
    //Layer 1 [[25][6]]
    ifstream in("eight.txt");
    int row = 6;
    int col = 25;
    char c;
    if(in.is_open()) {
        while(in.good()) {
            in.get(c);
            // Play with the data
            image_data.push_back(c-'0');
        }
    }
    int size = image_data.size();
    //number of layers = size / (23*6)
    int layers = size / (row * col);
    int fewest = INT_MAX;
    int count = 0;
    int l = 0;
    for(int i = 0; i < layers; i ++){
        int zeros = 0;
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                int x = image_data.at(count);
                if(x == 0){
                    zeros += 1;
                }
                
                count++;
            }
        }
        if(zeros < fewest){
            fewest = zeros;
            l = i;
        }
    }
    int loc = (l) * (row *col);
    int xcount = 0;
    int ycount = 0;
    for(int r = 0; r < row; r++){
        for(int c = 0; c < col; c++){
            int x = image_data.at(loc);
            if(x == 1){
                xcount++;
            }
            if(x ==2){
                ycount++;
            }
            loc++;

        }

    }
    cout << xcount * ycount << endl;

}