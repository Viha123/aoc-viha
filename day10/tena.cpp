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
    double num = -(thatY - myY);
    double den = thatX - myX;
    if(den == 0 && num > 0){

        return INT_MAX;
    }
    else if(den == 0 && num < 0){
        return INT_MIN;
    }
    else{
        return (num/den);
    }
}
bool calculate_dir(double myX, double myY, double thatX, double thatY){
    //true for right or up and false for left or down. 
    
    return !(thatX < myX);
    
}
struct point{
    double x;
    double y;
    bool operator==(const point& other){
        return (x == other.x && y == other.y);
    }
};
struct vec{
    point myP;
    point thatP;
    bool dir = calculate_dir(myP.x, myP.y, thatP.x, thatP.y);
    double slope = calculate_slope(myP.x, myP.y, thatP.x, thatP.y);
    bool operator==(const vec& other){
        return (slope == other.slope && dir == other.dir);
    }
    bool operator>(const vec& other){//true will mean this is greater and false will mean the other is greater
        //when is this vector greater than that vector
        //essentiall > and < will be the same, since this may end up being a black box for me in the future, 
        //i will make a similiar function that is operator <

        if(dir && !other.dir){ //this is true and that is false
            return true; 
        }
        else if(!dir && other.dir){
            return false;
        }
        else{ //if both are true
            //whichever has the larger slope will go first
            return (slope > other.slope);
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

struct great{
    bool operator()(const vec& other, const vec& current){ 
        if(current.dir && !other.dir){ //this is true and that is false
            return true; 
        }
        if(!current.dir && other.dir){
            return false;
        }
        if(current.dir && other.dir){ //if both are true
            //whichever has the larger slope will go first
            return (current.slope > other.slope);
        }
        else{
            return (current.slope > other.slope); //more negative it is the better
        }
    }
};

// struct greater1{
//     bool operator()(const vec &this, const vec &other){

//     };
// };


void get_laser_point(vector<point> &points, point &laserPoint){
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
                }
                else {
                    vecs.push_back(key);
                    count++;
                }
                
            }
            
        }
        if(count > max){
            max = count;
            laserPoint = ele;
        }
    }
}
vector<vec> hit_points(point p, vector<point> points){ //eventually turn hitpoint to .
    vector<vec> hitpoints;
    //start from top
    for(point ele2: points){
        if(ele2 == p){
            //do nothing
        }
        else{
            vec key = {p, ele2};
            bool anyof = false;
            for(int i = 0; i < hitpoints.size(); i ++){
                vec k = hitpoints.at(i);
                if(k == key){
                    anyof = true;
                    //compare manhattan distance from point cuz that easier
                    int dkey = abs(key.thatP.y-p.y) + abs(key.thatP.x - p.x);
                    int dk = abs(k.thatP.y-p.y) + abs(k.thatP.x - p.x);
                    if(dkey < dk){
                        //hitpoints.remove(dk)
                        hitpoints.erase(hitpoints.begin() + i);
                        //hitpoints.add(vector(dkey))
                        hitpoints.push_back(key);
                    }
                }
            }
            if(!anyof){
                hitpoints.push_back(key);
            }
        }
        
    }
    
    return hitpoints;

}
void removePoints(vector<point> &points, point &p){
    int index = 0;
    for(int i = 0; i < points.size(); i ++){
        if(points[i] == p){
            index = i;
        }
    }
    points.erase(points.begin() + index);
}
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

    point laserPoint; 
    get_laser_point(points, laserPoint);
    //get vector that establishes all first round hit points and changes them from # to . 
    //make vector into heap, if hit count less than 200 repeat step 1 and 2 and when count is greater than 200 pop until 200th element. 
    

    //TEST EXAMPLE
    
    int numPopped = 0;
    point bet;
    while(numPopped < 200){
        
        vector<vec> ps = hit_points(laserPoint, points);

        make_heap(ps.begin(), ps.end(), great());

        while(!ps.empty()){
        // cout << ps.front().thatP.x << ' ' << ps.front().thatP.y << endl;
            point toRemove = {ps.front().thatP.x, ps.front().thatP.y};
            removePoints(points, toRemove);
            pop_heap(ps.begin(), ps.end(), great());
            numPopped++;
            if(numPopped == 200){
                bet = toRemove;
                break;
            }
            ps.pop_back();
        }
    }
    cout << bet.x*100 + bet.y<< endl;

    


        

    //we have the laserpoint from which we want to start eliminating asteroids
    //take all the points that laserpoint will hit (vectors) and then organize them by heaps,keep popping
    //the heap 
    //TESTING == statement for vectors
    // point exp0 = {2,2};
    // point exp1 = {3,1}; //lets say this is the laser point
    // point exp2 = {4,2};
    // point exp3 = {3,0};
    // point exp4 = {2,0};
    // point exp5 = {3,3};

    // vec vec1 = {exp1,exp0};
    // vec vec2 = {exp1,exp2};
    // vec vec3 = {exp1,exp3};
    // vec vec4 = {exp1,exp4};
    // vec vec5 = {exp1,exp5};

    // vector<vec> tests;
    // tests.push_back(vec1);
    // tests.push_back(vec2);
    // tests.push_back(vec3);
    // tests.push_back(vec4);
    // tests.push_back(vec5);


    // make_heap(tests.begin(), tests.end(), great());
    // while(!tests.empty()){
    //     std::cout << tests.front().thatP.x << ' ' << tests.front().thatP.y << endl;
    //     std::pop_heap(tests.begin(), tests.end(), great());
    //     tests.pop_back();

    // }
    // cout << vec4.slope << endl;



}