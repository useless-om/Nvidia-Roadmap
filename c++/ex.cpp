# include <iostream>
# include <stack>
# include <string>
using namespace std;

string revstr(string input){
    stack<char> s;
    for(char ch: input){
         s.push(ch);
    }

    string rev = "";
    while(!s.empty()){
        rev = rev + s.top();
        s.pop();
    }

    return rev;
}

int main(){

    string original = "NarutoUzumaki";
    string reversed = revstr(original);

    cout << "Original: " << original << endl;
    cout << "Reversed: " << reversed << endl;

return 0;
}

