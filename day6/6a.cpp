#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

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
    
    // std::unordered_set<Node, Node::node_hash> node_set;

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
    int sum = 0;
    for(auto i: map)
    {
        // cout << i.first.name << " orbits " << i.second.name << endl;
        //i.second is next
        Node current = i.second;
        int c = 1;
        while(map.count(current) != 0)
        {
            c++;
            current = map.find(current)->second;
        }
        sum += c;
    }
    cout << sum << endl;
}