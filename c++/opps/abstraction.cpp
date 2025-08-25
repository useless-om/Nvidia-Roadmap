# include <iostream>
using namespace std;

/* ABSTRACT CLASS*/
 class shape {
    virtual void draw() = 0; //PURE VIRTUAL FUNCTION
 };

class Circle : public shape {

    public:
      void draw() override {
          cout<<" drawing a circle\n";
      }
};

int main(){

    Circle c1;
    c1.draw();
    

    return 0;
}
