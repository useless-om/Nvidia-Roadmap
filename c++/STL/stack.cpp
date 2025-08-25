// STACK also called as last in first out data structure

# include <iostream>
# include <vector>
# include <stack>
# include <string>


using namespace std;

int main(){

    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);

    while(!s.empty()){
        cout<<s.top()<<" ";

        s.pop();
    }
    cout<<endl;

    stack<int> s1;
    s1.push(1);
    s1.push(2);
    s1.push(3);
    stack<int> s2;
    s2.swap(s1); // all values of s wil come in s2

    cout<<"size of s1: "<<s1.size()<<endl;
    cout<<"size of s2: "<<s2.size()<<endl;




    stack<string> st;
    
    string str; 
    int i= 1;
    while (true)
    {   
         cout<<" enter the string "<<i<<": ";
         cin>>str;
         st.push(str);
         if(str=="undo"){
            if(!st.empty()){
                cout<<"undo: "<<st.top()<<endl;
                st.pop();
            }
         }
        
    }
    
    
    return 0;
}