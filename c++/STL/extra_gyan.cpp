#include <iostream>
#include <sstream>
using namespace std;

int main() {
// What is stringstream in simple terms?

// Think of it as a "string version of cin/cout":

// cin reads from keyboard.

// stringstream reads from a string.
    
string text = "apple banana apple mango";
stringstream ss(text);  // Load string into stream
    
string word;
    while (ss >> word) {  // Extract word by word
        cout << word << endl;
    }
}
