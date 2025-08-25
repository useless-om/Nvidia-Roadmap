# include <iostream>
# include <vector>
using namespace std;

int main(){

    vector<int> v;
    int i=0;
    cout<<"enter the number in vecter "<<endl;
    cout<<" -1 to terminate"<<endl;
    
    while(true){
        cout<<" enter the value in vector: ";
        cin>>i;
        if(i==-1)
            break; 
        v.push_back(i);
}
    for(auto it = v.begin(); it!=v.end();it++){
        cout<<*(it)<<" ";
    }

    return 0;
}