#include <iostream>
using namespace std;

// f(x) = x^2 + 2
int add(int a, int b)
{
    int c;
    c = a+b;
    return c;
}

int main(){

    int a, b;
    cout<<"enter 1st number "<<endl;
    cin>>a;
    cout<<"enter 2nd number "<<endl;
    cin>>b;
    cout<<"the function is "<<add(a,b)<<endl;

    return 0;
}