#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <SFML/Graphics.hpp>

using namespace std;

int main(){
    enum color
    {
        black = 0,
        white = 1,
        transparent = 2
    };
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
    //PART 1 ----------------------------------
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
    // cout << xcount * ycount << endl;
    int image[row][col];
    //PART 2 ------------------------------------------------
    //convert image_data into 3d array;
    int layered_image[col][row][layers];
    int i = 0;
    cout << "BEGINNING OF PART 2" << endl;
    for(int l = 0; l < layers; l++){
        for(int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                layered_image[c][r][l] = image_data.at(i);
                i++;
                // cout << layered_image[c][r][l];
            }
            // cout << endl;
        }
        // cout << endl;
    }
    //image_data converted into 3d array
    //convert 3d array into 2d array according to constraints
    for(int r = 0; r < row; r++){
        for(int c = 0; c < col; c++){
            for(int l = 0; l < layers; l++){
                if(layered_image[c][r][l] != transparent){
                    image[r][c] = layered_image[c][r][l];
                    break;
                }
            }
        }
    }

    for(int r = 0; r < row; r++){
        for(int c = 0; c < col; c++){
            cout << image[r][c];
        }
        cout << endl;
    }
    
    // //draw array using SFML graphics?
    sf::RenderWindow window(sf::VideoMode(col*20, row*20), "MESSAGE!");
    while(window.isOpen()){
        for(int r = 0; r < row; r ++){
            for(int c = 0; c < col; c++){
                int color = image[r][c];
                sf::RectangleShape rect(sf::Vector2f(20,20));
                int xpos = c*20;
                int ypos = r*20;
                rect.setPosition(xpos,ypos);
                if(color == black){
                    rect.setFillColor(sf::Color(0,0,0));
                }
                else{
                    rect.setFillColor(sf::Color(255,255,255));
                }
                window.draw(rect);
                window.display();
            }
        }


    }


}  