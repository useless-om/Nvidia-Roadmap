# include <iostream>
#include <string>
using namespace std;

// class person {
// public :
//    string name;
//    int age;
// };


// class student :public person{
// public:
//     int rollno;
// };

// /*multi level inheritance*/
// class gradStudent : public student{
// public:
//      string researcharea;

// };

// int main(){
     
//     gradStudent s1;
//     s1.name="tony stark";
//     s1.researcharea =" time travel";
//     cout<<s1.name<<endl;
//     cout<<s1.researcharea;

//     return 0;

// }






// /*multiple inheritance*/
// class student {
// public:
//        string name;
//        int rollno;
// };

// class teacher {
// public:
//        string subject;
//        double salary;   
// };

// class TA : public student ,public teacher{

// };

// int main(){

//     TA t1;
//     t1.name ="om";
//     t1.subject = "subject";

//     cout<<t1.name<<endl;
//     cout<<t1.subject;

//     return 0;
// }



/* heiarcy inherytance*/
class Person{
    public:
    string name;
    int age;
};

class Student : public Person{
    public:
    int rollno;
};

class Teacher : public Person{
    public:
    string subject;
};




// /*hybrid inheritance*/ mixture of all inheritance