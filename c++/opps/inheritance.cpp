# include <iostream>
# include <string>
using namespace std;

// class person {

//     public:
//     string name;
//     int age;

//     person() {
//        cout<<"parent/base constructor"<<endl;
//     }
// };

// class student : public person {
//      public :
//      int roll_no;

//      void print(){
//     cout<<"child constructor"<<endl;
//     cout<<" name: "<<name<<endl;
//     cout<<" age: "<<age<<endl;
//     cout<<"roll no: "<<roll_no<<endl;
// }

// };



class person {

    public:
    string name;
    int age;

    person(string name, int age) {
        this->name=name;
        this->age=age;
       
    }
};

// class student : person {
//     public :
//     int roll_no;
    
//     student(string name, int age,int rollno) : person(name, age){
//         this->roll_no=rollno;
//     }
//     void print(){
//     cout<<"child constructor"<<endl;
//     cout<<" name: "<<name<<endl;
//     cout<<" age: "<<age<<endl;
//     cout<<"roll no: "<<roll_no<<endl;
// }

// };




    // modes

class student : public person {
    public :
    int roll_no;
    
    student(string name, int age,int rollno) : person(name, age){
        this->roll_no=rollno;
    }
    void print(){
    cout<<"child constructor"<<endl;
    cout<<" name: "<<name<<endl;
    cout<<" age: "<<age<<endl;
    cout<<"roll no: "<<roll_no<<endl;
}

};

int main(){
    
    /*for 1st code at top for defaul constructor*/
    // student s1;
    // s1.name="om";
    // s1.age=19;
    // s1.roll_no=1;
    // s1.print();


    /* 2nd code*/
    // student s1("Aizen",25,1882);
    // s1.print();




    


    return 0;
    
}