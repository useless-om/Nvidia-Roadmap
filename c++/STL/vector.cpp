// VECTOR - DYNAMIC ARRAY i.e WHEN ARR IS FILLED IT DOUBLES IT SIZE IF WE TRY TO FILL MORE ELEMENTS

# include <iostream>
# include <vector>
using namespace std;

int main(){

    vector<int> v;
    cout<<" capacity->,"<<v.capacity()<<endl;
    
    v.push_back(1);
    cout<<" capacity->,"<<v.capacity()<<endl;

    v.push_back(2);
    cout<<" capacity->,"<<v.capacity()<<endl;

    v.push_back(3);
    cout<<" capacity->,"<<v.capacity()<<endl;

    cout<<"size-> "<<v.size()<<endl;
    cout<<"element at 2nd index-> "<<v.at(2)<<endl;
    cout<<"front-> "<<v.front()<<endl;
    cout<<"back-> "<<v.back()<<endl;

    cout<<" befor pop"<<endl;
    for( int i :v){
        cout<<i<<" ";
    } cout<<endl;

    v.pop_back();
    for( int i :v){
        cout<<i<<" ";
    } cout<<endl;

    v.clear(); /* AFTER CLEAR SIZE BECOMES ZERO*/


    vector<int> a(5,1); /*<- at fiest it will contain 5 elem and all initialized with 1*/
    for(int i :a){
        cout<<i<<" ";
    }cout<<endl;
     
    vector<int> b(a);
    for(int i :b){
        cout<<i<<" ";
    }cout<<endl;
     

    vector<int> c = {2,3,1};






    // ITERATORS
    vector<int> v1 = {1,2,35,2,4};

    cout<<"vec.end "<< *(v1.end())<<endl; // end give the value after the last element (garbage)
    cout<<"vec.begin "<<*(v1.begin())<<endl;
    

    vector<int>::iterator it;
    // FORWARD 
    for(it= v1.begin(); it!= v1.end(); it++){
        cout<<*(it)<<" ";
    } cout<<endl;
    
    // BACKWARD
    for(auto it= v1.rbegin(); it!= v1.rend(); it++){
        cout<<*(it)<<" ";
    } cout<<endl;
    


    return 0;
}