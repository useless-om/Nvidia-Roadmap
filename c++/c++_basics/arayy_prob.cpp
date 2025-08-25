# include <iostream>
using  namespace std;

int main(){
    int n;
    cout<<"enetr the number of elements in array: ";
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cout<<"enter the value of "<<i<<"th element: ";
        cin>>arr[i];
    }

    cout<<"to check the largest element"<<endl;
    int temp =arr[0];
    for (int i = 0; i<n;i++){
        if(arr[i]>temp){
            temp=arr[i];
        }
      
            }
    cout<<"the largest ele is: "<<temp;

        return 0;
        
        }
    



