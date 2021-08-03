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
    int x;
    A () {}
    A (int x_)
    {
        x = x_;
    }

    int sum ()
    {
        return x; 
    }

    virtual void print ()
    {
        std::cout << "A::print()" << std::endl;
    }
};

//========================================================================

class B : public A
{
    public:
    int y;
    B () {}
    B (int x_, int y_)
    {
        x = x_;
        y = y_;
    }

    int sum ()
    {
        return x + y; 
    }

    virtual void print ()
    {
        std::cout << "B::print()" << std::endl;
    }
};

//========================================================================

class C : public B
{
    public:
    int z; 
    C (int x_, int y_, int z_)
    {
        x = x_;
        y = y_; 
        z = z_;
    }

    int sum ()
    {
        return x + y + z; 
    }

    virtual void print ()
    {
        std::cout << "C::print()" << std::endl;
    }
};

//========================================================================

 void print (A* a)
{
    std::cout << a->sum () << std::endl;
}

 void print (B* b)
{
    std::cout << b->sum () << std::endl;
}

 void print (C* c)
{
    std::cout << c->sum () << std::endl;
}

// 2 0 1 
int sum (C* a, C* b, C* c)
{
    std::cout << "4 steps" << std::endl; 
    return b->x + a->x + c->x;
}

// 2 2 0
int sum (A* a, A* b, C* c)
{
    std::cout << "5 steps" << std::endl; 
    return a->x + b->x + c->x;
}

void func (B* a)
{
    a->print ();
}

//========================================================================

int 
main() 
{
    
    
    C* c = new C(7, 3, 21);

    print (c);

    std::cout << sum (c, c, c) << std::endl; 

    func ((B*)c);

}


//========================================================================



