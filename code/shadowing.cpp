// Kattis Solution 
// Author: Amy Burnett
//========================================================================
// Includes 

#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <unordered_map>
#include <map>
#include <list>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cmath>

//========================================================================
// Library functions 

class A
{
    public:
    int val;
    int z; 

    A ()
    {
        val = 0;
        z = 1; 
    }
};

class B : public A
{
    public:
    int x;
    int y;
    // this val hides/shadows A's val 
    // B still contains A's val but it is inaccessable due to shadowing 
    double val; 

    B ()
    {
        x = 10;
        y = 42;
        val = 0.5;
    }
};

void 
func (A a)
{
    std::cout << a.val << " " << a.z << std::endl;
}

//========================================================================

int 
main() 
{
    
    B b;

    b.val = 3.14;
    b.z = 21;

    func (b);

    std::cout << b.val << " " << b.z << std::endl;
    

}


//========================================================================




