# include <iostream>
// #include "hero.cpp"
using namespace std;
class hero {
        // properties

       
        // private: /*class ke andar sirf access kr skte h*/
        private :
        int health;

        public:
         char level;
        char name[100];

         /*this void does the cout of level and does not display so as if level has wrong inpput then too program runs*/
        void print(){
            cout<< level << endl;
        }
        int gethealth(){
            return health;
        }
        char getlevel(){
            return level;
        }
        /*also can set password with ifelse*/
        void sethealth(int h, char pass){ 
           
            if(pass=='om'){
                health=h;
            }
           
        }
        void setlevel(char ch){
            level = ch;
        }
};

int main(){
    // creation of object
    // hero h1;
    // cout<<" size :"<< sizeof(h1)<<endl;

    // hero om;

    // // om.health=69; not possible due to private
    // om.sethealth(69,'om');
    // om.level= 'A';
    // cout<<"health of om is : "<<om.gethealth()<<endl;
    // cout<<"level is: "<<om.level<<endl;



    // static allocation
    hero a;  
    cout<<" level is "<<a.level<<endl;
    cout<<"health is "<<a.gethealth()<<endl;

    // dyanmically
    hero *b = new hero;
    cout<<" level is "<<(*b).level<<endl;
    cout<<" health is "<<(*b).gethealth()<<endl;
    return 0;
}