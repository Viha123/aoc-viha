#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <typeinfo>
#include <array>
#include <bits/stdc++.h>
#include <limits.h>
#include <stdlib.h>
using namespace std;

class Segment
{
    public:
        int start[2] = {1,1}; //x,y
        int end[2];
        char type;
        int length; 

        Segment(int st[2], char dir, int length)
        {
            start[0] = st[0];
            start[1] = st[1];
            type = dir;
            if(dir == 'D')
            {
                end[0] = start[0];
                end[1] = start[1] - length;
            }
            if(dir == 'U')
            {
                end[0] = start[0];
                end[1] = start[1] + length;
            }
            if(dir == 'R')
            {
                end[0] = start[0]  + length;
                end[1] = start[1];
            }
            if(dir == 'L')
            {
                end[0] = start[0]  - length;
                end[1] = start[1];
            }
        }
            

        int * getEnd() 
        {
            static int end_to_return[2];
            end_to_return[0] = end[0];
            end_to_return[1] = end[1];
            return end_to_return;
        }
        int * getStart() 
        {
            static int start_to_return[2];
            start_to_return[0] = start[0];
            start_to_return[1] = start[1];
            return start_to_return;
        }
        char getType()
        {
            return type;
        }
        int getLength()
        {
            return length;
        }
};
void convert_to_vector(vector<string> &outputs, string content);
void convert_to_segments(vector<string> &outputs, std::vector<Segment> &wires, int initial[]);
bool check_in_between(int num, int bound1, int bound2);
int calc_distance(int x, int y, int w, int z);
int num_steps(int i, vector<Segment> wire, int stopx, int stopy);
int main()
{
    //step one parse the input
    std::ifstream data_file("three.txt");
    int initial[2] = {1,1};
    string contents1;
    string contents2;
    vector<string> outputs1;
    vector<string> outputs2;

    std::vector<Segment> wireA;
    std::vector<Segment> wireB;

    if(data_file.is_open())
    {
        getline(data_file,contents1);
        getline(data_file,contents2);
    }

    convert_to_vector(outputs1, contents1);
    convert_to_vector(outputs2, contents2);

    convert_to_segments(outputs1, wireA, initial);
    initial[0]=1;
    initial[1] =1;//reinitialize everything
    cout << "check here" << endl;
    convert_to_segments(outputs2, wireB, initial);
    
    int distance = INT_MAX;
    for(int i = 0; i < wireA.size(); i ++)
    {
        Segment s = wireA.at(i);
        for(int j = 0; j < wireB.size(); j ++)
        {
            Segment m = wireB.at(j);
            int * marrstart = m.getStart();
            int * marrend = m.getEnd();
            int mxstart = *(marrstart + 0);
            int mystart = *(marrstart + 1);
            int mxend = *(marrend + 0);
            int myend = *(marrend + 1);

            int * sarrstart = s.getStart();
            int * sarrend = s.getEnd();
            int sxstart = *(sarrstart + 0);
            int systart = *(sarrstart + 1);
            int sxend = *(sarrend + 0);
            int syend = *(sarrend + 1);
            // cout << sxstart << systart << sxend << syend << mxstart << mystart << mxend << myend << endl;
            if((s.type == 'R' || s.type == 'L') && (m.type == 'U' || m.type == 'D'))
            {
                if(check_in_between(mxstart, sxstart, sxend) && check_in_between(systart,mystart, myend))
                {
                    //we've got intersections here
                     
                    if(mxstart != 1 && systart != 1){
                        int dist = num_steps(i, wireA, mxstart, systart) + num_steps(j, wireB, mxstart,systart);
                        // cout << mxstart << " " << systart << endl;
                        if(dist < distance)
                        {
                            distance = dist;
                        }
                        
                    }
                    
                }
            }
            if((s.type == 'U' || s.type == 'D') && (m.type == 'L' || m.type == 'R'))
            {

                if(check_in_between(sxstart, mxstart, mxend) && check_in_between(mystart, systart, syend))
                {
                    //we've got intersections here, need to calculate steps instead of distance now
                    if(sxstart != 1 && mystart != 1){
                        int dist = num_steps(i, wireA, sxstart, mystart) + num_steps(j, wireB, sxstart,mystart);
                        // cout << mxstart << " " << systart << endl;
                        if(dist < distance)
                        {
                            distance = dist;
                        }
                    }
                    
                }
            }
            
        }
    }
    cout << distance << endl;

}
void convert_to_vector(vector<string> &outputs, string content)
{
    stringstream ss1(content);
    while (ss1.good())
    {
        string substr;
        getline(ss1, substr, ',');
        outputs.push_back(substr);
    }
}

void convert_to_segments(vector<string> &outputs, std::vector<Segment> &wires, int initial[])
{
    for(string i: outputs) //converting into segments
    {
        char dir = i.front();
        string str = i.substr(1);
        int n = stoi(str);
        cout << initial[0] << " " << initial[1] << endl;
        Segment seg(initial, dir, n);

        wires.push_back(seg);
        int *start = seg.getEnd(); //end is the new beginning (so profound)
        initial[0] = *(start+0);
        initial[1] = *(start + 1);  
        cout << initial[0] << " " << initial[1] << endl;
     
    }
}
int num_steps(int i, vector<Segment> wire, int stopx, int stopy)
{
    int sum = 0;
    for(int j = 1; j <= i; j ++)
    {
        Segment seg = wire.at(j);
        int * segx = seg.getStart();
        int x = *(segx + 0);
        int y = *(segx + 1);
        Segment prev = wire.at(j-1);
        int * segprev = prev.getStart();
        int xprev = *(segprev + 0);
        int yprev = *(segprev + 1);

        int dist = calc_distance(x,y,xprev, yprev);
        sum += dist;
        if(j == i)
        {
            int toAdd = calc_distance(stopx,stopy, x, y);
            sum+=toAdd;
        }

    }
    return sum;
}
int calc_distance(int x, int y, int w, int z)
{
    return (abs((x-w)) + abs(y-z));
}
bool check_in_between(int num, int bound1, int bound2)
{
    int small = min(bound1,bound2);
    int big = max(bound1, bound2);
    if( num >= small  && num <= big){
        return true;
    }
    else{
        return false;
    }
}