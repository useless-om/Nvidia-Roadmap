# include <iostream>
# include <string>
using namespace std;

class bankacc_class
{
private:
    string owner;
    float balance;
public:
       
bankacc_class() {
    cout<<" Default cinstructor"<<endl;
}

bankacc_class(string n, float b){
    this-> owner = n;
    this -> balance = b;
}
void print(){
    cout<<" yokoso watashino soul society bank"<<endl;
    cout<<" owner: "<<owner<<endl;
    cout<<"BALANCE: "<<balance<<endl;
}
void setname(string n){
    owner = n;
}
void setbalance(float b){
    balance = b;
}

};

int main(){
    bankacc_class a1;
    a1.setname("om pawar");
    a1.setbalance(22522);

    a1.print();
    
    bankacc_class a2("Soske Aizen", 999999.999);
    a2.print();

    

            
}



