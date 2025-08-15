# include <iostream>
using namespace std;
class hero {

       
        private :
        int health;

        public:
         char level;
        
        hero(){
            cout<<" constructor called"<<endl;
        }

        // Parameterised constructor
        hero(int health){
           this -> health = health;
           cout<<"this "<<this<<endl; /*this is pointer which sets the objects health*/
        }

        hero(int health , char level){
            this -> health = health;
            this -> level = level;
        }

        // copy connstructor
        hero(hero& temp){
            cout<<"copy constructor called"<<endl;
            this-> health= temp.health;
            this-> level = temp.health;
        }

        void print(){
            cout<< level <<this->level<< endl;
            cout<< "health: "<<this->health<<endl;

        }
        int gethealth(){
            return health;
        }
        char getlevel(){
            return level;
        }
        
        void sethealth(int h){
             health=h;     
        }
        void setlevel(char ch){
            level = ch;
        }
};

int main(){

    // hero om(66);
    // cout<<" adresss : "<<&om<<endl;

    // // dyanmicaly
    // hero *b = new hero(22);
    // b->print();

    // hero temp(22,'C');
    // temp.print();
    
     

    // copy constructor

    hero luffy(99,'A');
    luffy.print();

    hero zoro(luffy); /*copy*/
    zoro.print();

    return 0;
}