# include <iostream>
using namespace std;

int main(){

    int n;
    cout<<"enter a number to check if it is armstrong no. or not : "<<endl;
    cin>>n;
    int temp = n;
    int sum =0;
    while (n>0)
    {
         sum = sum + (n%10)*(n%10)*(n%10);
         n = n/10;
    }
    
    if(temp==sum){
        cout<<"the number is armstronf"<<endl;
    }
    else{
        cout<<" not armsstrong";
    }
    
    
           
    return 0;
}