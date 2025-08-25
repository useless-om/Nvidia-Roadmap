# include <iostream>
using namespace std;


/*CONSTRUCTOR OVERLOADING*/ /*how the constructor behaves acc to use*/
// class Student{
      
//     public :
//          string name;
//     Student(){
//         cout<<"non parenthesi constyructoe"<<endl;

//     }
//     Student(string name){
//         cout<<"parentehsize consteuctor"<<endl;
//         this -> name=name;

//     }
// };

// int main(){
//     Student s1("gandu");
//     Student s2;

//     return 0;
// }



/* FUNCTION OVERLOADING*/

// class Print {
//     public:
//     void show(int n){
//         cout<<" int: "<<n<<endl;
//     }

//     void show(char ch){
//         cout<<"char: "<<ch<<endl;
//     }
// };
// int main(){

//     Print p1;
//     p1.show(233);
//     p1.show('s');
// }



/*RUNTIME POLYMORPISM*/

/*FUNCION OVERRIDING*/ /* staic biding */

// class Parent {
//     public:
//     void getinfo(){
//         cout<<"parent"<<endl;
//     }
// };

// class Child : public Parent {
//     public:
//     void getinfo(){
//         cout<<"child"<<endl;
//     }
// };

// int main(){

//     Child c1;
//     c1.getinfo();

//     Parent p1;
//     p1.getinfo();

//     return 0;
// }



/* VIRTUAL FUNCTION*/  /* at runtime and also if we do dyanamic */

class Parent {
    public:
    void getinfo(){
        cout<<"parent"<<endl;
    }
    virtual void hello(){
        cout<<" hi this is parent"<<endl;
    }
};

class Child : public Parent {
    public:
    void getinfo(){
        cout<<"child"<<endl;
    }
    void hello(){
        cout<<" hi this is child"<<endl;
    }
};

int main(){

    Child c1;
    c1.hello();
    return 0;
}