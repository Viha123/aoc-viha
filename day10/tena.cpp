#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
#include <limits>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

//struct vector 
//struct point
void get_data(vector<vector<char>> &data){

    ifstream in("ten.txt");
    //put into 2d array of chars
    vector<char> line;

    if(in.is_open()){
        while(in.good())
        {
            char c;
            in.get(c);
            if(c =='\n'){
                data.push_back(line);
                line.clear();
            }
            else{
                line.push_back(c);
            }
        }
        
    }
    data.push_back(line);

    
}
void traverse_data(vector<vector<char>> &data){ //helper
    for(int r = 0; r < data.size(); r++){
        for(int c = 0; c < data[0].size(); c++){
            cout << data[r][c];
        }
        cout << endl;
    }
}
double calculate_slope(double myX, double myY, double thatX, double thatY){
    double num = thatY - myY;
    double den = thatX - myX;
    if(den == 0){
        return INT_MAX;
    }
    else{
        return (num/den);
    }
}
bool calculate_dir(double myX, double myY, double thatX, double thatY){
    //true for right or up and false for left or down. 
    if(thatX > myX){
        return true;
    }
    else if(thatX < myX){
        return false;
    }
    else if(thatY > myY){
        return true;
    }
    else{
        return false;
    }
}
struct point{
    double x;
    double y;
    bool operator==(const point& other){
        if(x == other.x && y == other.y){
            return true;
        }
        else{
            return false;
        }
    }
};
struct vec{
    point myP;
    point thatP;
    bool dir = calculate_dir(myP.x, myP.y, thatP.x, thatP.y);
    double slope = calculate_slope(myP.x, myP.y, thatP.x, thatP.y);
    bool operator==(const vec& other){
        if(slope == other.slope && dir == other.dir){
            return true;
        }    
        else{
            return false;
        }
    }
};

struct compare
{
    vec key;
    compare(vec const &i): key(i) {}
 
    bool operator()(vec const &i) {
        if(key.slope == i.slope && key.dir == i.dir){
            return true;
        }    
        else{
            return false;
        }
    }
};
int main(){
    vector<vector<char>> data;
    get_data(data);
    // traverse_data(data); //data in 2d array
    // unordered_set<point> points;
    vector<point> points;
    for(int r = 0; r < data.size(); r++){ 
        for(int c = 0; c < data[0].size(); c++){
            // cout << data[r][c];
            if(data[r][c]=='#'){

                struct point p1 = {c, r};
                points.push_back(p1);
            }
        }
        // cout << endl;
    }
    //
    int max = INT_MIN;
    for(point ele: points){
        // cout << ele.x << ele.y << endl;
        //make a hashset of vec class will need to see how to make vec equal
        vector<vec> vecs;
        int count = 0;
        for(point ele2: points){
            if(ele2 == ele){
                //do nothing
            }
            else{
                vec key = {ele, ele2};
                //check if key exists in the vector already
                if (std::any_of(vecs.begin(), vecs.end(), compare(key))) {
                    //do nothing
                }
                else {
                    vecs.push_back(key);
                    count++;
                }
            }
            
        }
        if(count > max){
            max = count;
        }


    }
    cout << max << endl;
    //TESTING == statement for vectors
    // point exp0 = {0,0};
    // point exp1 = {3,1};
    // point exp2 = {2,4};
    // vec vec1 = {exp0,exp1};
    // vec vec2 = {exp0,exp2};
    // cout << vec1.slope << endl;
    // vector<vec> tests; 
    // tests.push_back(vec1);
    // cout << tests.find(vec2) << endl;


    

}