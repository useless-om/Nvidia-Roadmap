# include <iostream>
# include <string>
using namespace std;

class student {

    private:
     string name;
     int age;
     char grade;


    public:

    void setdetails(string n,int a,char g){
        name=n;
        age=a;
        grade=g;
    }
    void introduce(){
        cout <<" name: "<<name<<endl;
        cout<<"age: "<<age<<endl;
        cout<<"grade: "<<grade<<endl;

    }
    
                
};

int main(){
    
    student s1;
    s1.setdetails("Zoro",25,'A');

    student s2;
    s2.setdetails("sanji",23,'b');

    s1.introduce();
    s2.introduce();

    return 0;

}