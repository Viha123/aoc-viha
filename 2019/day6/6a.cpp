#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <limits.h>
#include <chrono>
using namespace std;
class Node 
{
    public:
        string name;
        int length; 
        Node(string n)
        {
            name = n;
            length = 0; //just do node.length++
        }
        void setLength(int len)
        {
            length = len;
        }
        bool operator==(const Node& other) const
        { 
            if (this->name == other.name) return true;
            else return false;
        }
        struct node_hash {
            std::size_t operator()(const Node& _node) const {
                return std::hash<std::string>()(_node.name);
            }
        };
};
int main()
{
    
    auto start = chrono::high_resolution_clock::now();
    fstream data("six.txt");
    int pl = 3;// planet lenght, change to 3 later
    unordered_map<Node, Node, Node::node_hash> map;
    if(data.is_open()){
        while(data.good())
        {
            string content;
            data >> content;

            string name = content.substr(0,pl);
            string orbit = content.substr(pl + 1); //A)B -> B orbits A. 

            Node a(name);

            Node b(orbit);
            
            map.insert(make_pair(b, a));

            
        }
    }
    // int sum = 0;
    // for(auto i: map)
    // {
    //     // cout << i.first.name << " orbits " << i.second.name << endl;
    //     //i.second is next
    //     Node current = i.second;
    //     int c = 1;
    //     while(map.count(current) != 0)
    //     {
    //         c++;
    //         current = map.find(current)->second;
    //     }
    //     sum += c;
    // }
    // cout << "All direct and indirect orbits: " << sum << endl;
    int sum = 0;
    for(auto [key, value]: map)
    {
        Node current = value;
        int c = 1;
        while(map.count(current)!=0){
            c++;
            current = map.find(current)->second;
        }
        sum+=c;
    }

    unordered_set<Node, Node::node_hash> node_set;

    //add all nodes that associate with YOU
    Node you("YOU");
    int l = 0;
    
    while(map.count(you)!=0)
    {
        you = map.find(you)->second;
        l++;
        you.setLength(l);
        node_set.insert(you);
    }
    //PART B
    Node sam("SAN");
    int s = 0;
    int transfer = INT_MAX;
    while(map.count(sam)!=0)
    {
        
        sam = map.find(sam)->second;
        s++;
        sam.setLength(s);
        if(node_set.count(sam))
        {
            auto y = node_set.find(sam);
            int ylen = y->length;
            if(transfer > (ylen + sam.length-2))
            {
                transfer = ylen+sam.length -2; //account for ob1 errors in both
            }
            
        }
    }
    cout << transfer << endl;
    auto stop = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::milliseconds>(stop-start);
    cout << duration.count() << endl;

}