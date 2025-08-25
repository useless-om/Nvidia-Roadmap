# include <iostream>
# include <string>
using namespace std;

class Pokemon {
private:
        int health;
public :
        string name;
    
    void sethealth(int h, string password){
       if (password=="om")
       {
          this ->health=h;
       }
       else {
        cout<<" incorrect pass or pass not set"<<endl;
       }
       
        
    }
     void gethealth(){
        cout<<" the health of "<<name<<" is: "<<health<<endl;
     }
       
};

int main(){

    Pokemon p1;
    
p1.name = " pikachu";
p1.sethealth(89,"om");
p1.gethealth();

    return 0;
}