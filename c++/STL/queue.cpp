# include <iostream>
# include <vector>
# include <stack>
# include <queue> //FIRST IN FIRST OUT
# include <string>
using namespace std;

int main(){

    queue<int> q;

    q.push(1);
    q.push(2);
    q.push(3);

    cout<<"the back value: "<<q.back()<<endl;


    while(!q.empty()){
         cout<<q.front()<<" ";
         q.pop();
    }



    

    return 0;
}