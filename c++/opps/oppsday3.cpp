# include <iostream>
# include <string>
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
           
            if(pass=='o'){
                health=h;
            }
           
        }
        void setlevel(char ch){
            level = ch;
        }
};
int main(){
    //  statically
    hero a;
    a.sethealth(33,'o');
    a.setlevel('A');
    cout<<" level is "<<a.level<<endl;
    cout<<" health is "<<a.gethealth()<<endl;
    

    // dyanamically
    hero *b = new hero; 
    b->setlevel('b');
    b->sethealth(88,'o');

    cout<<" level of b is "<<(*b).level<<endl;
    cout<<" health of b is "<<(*b).gethealth()<<endl;
     
     cout<<" level of b is "<<b->level<<endl;
    cout<<" health of b is "<<b->gethealth()<<endl;
    return 0;
}
