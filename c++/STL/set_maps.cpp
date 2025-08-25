# include <iostream>
# include <set> 
# include <map>
using namespace std;

// SET -> - Stores unique elements in sorted order.
//- No duplicates allowed.
//- Internally uses a balanced BST.

int main(){
     
    set<int> s;

    s.insert(1);
    s.insert(1);
    s.insert(3);
    s.insert(5);
    s.insert(5);
    s.insert(6);
    s.insert(0);

    for(auto i:s){
        cout<<i<<endl;
    }cout<<endl;

    s.erase(1);

    for(auto i:s){
        cout<<i<<endl;
    }cout<<endl;

    cout<<"5 is present or not-> "<<s.count(5)<<endl;
    //  RETURNS 1 IF YES -> count()
     cout<<"5 is present or not-> "<<s.count(-5)<<endl;
    
     set<int>::iterator itr = s.find(5);
     // HERE WE GET THE REFERENCE OF ITERATOR AT 5 SO THAT WE CAN USE IT TO COUT THE VALUES AFETR 5 or befor 5

    for(auto it=itr;it!=s.end();it++){
        cout<<*it<<endl;
    }cout<<endl;


     s.size(); // no. of elements
     cout<<"the size is: "<<s.size()<<endl;
     cout<<endl;
     s.clear(); // removes all elements
    










     /* MAPS*/
    //  - Stores key-value pairs: each key is unique, and maps to a value.
    //  - Internally implemented as a balanced binary search tree (usually Red-Black Tree).
    //  - Keys are sorted in ascending order by default.

    map<int,string> m;
    
    m[1] = "luffy";
    m[12] = "zoro";
    m[3] = "sanji";
    
    cout<<m[3]<<endl;
    cout<<endl;
    m.insert({5,"robin"});
for(auto& i:m){
    cout<<i.first<<":"<<i.second<<endl;    
}

cout<<"finding: "<<m.count(12)<<endl;

m.erase(12); //erase key-value pair at 12
m.size(); // no. of elements
// m.clear();

auto it = m.find(3); //iterator setting

for(auto i=it;i!=m.end();i++){
    cout<<(*i).first<<":"<<(*i).second<<endl;
}

    return 0;

      
}