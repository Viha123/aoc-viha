#include <iostream>
#include <fstream>
#include <string>
int main()
{
    std::ifstream myFile("1a.txt");
    std::string contents;
    int sum = 0;
    if(myFile.is_open())
    {
        while(myFile.good())
        {
            myFile >> contents;
            int num = stoi(contents);
            num = num/3;
            num -= 2;
            int fuel = num;
            while(fuel > 0)
            {
                fuel = fuel/3;
                fuel -= 2;
                if(fuel < 0){
                    fuel = 0;
                }
                sum += fuel;
            }
            sum +=num;
        }
        // int fuel = sum;
        // while(fuel > 0)
        // {
        //     fuel = fuel/3;
        //     fuel -= 2;
        //     if(fuel < 0){
        //         fuel = 0;
        //     }
        //     sum += fuel;
        // }
        std::cout<<sum<<std::endl;

    }
}