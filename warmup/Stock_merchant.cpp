#include <iostream>
#include <algorithm>
#include <vector>

int main(){
    int n;
    std::cin >>n;
    std::vector<int> arr;
    for(int i = 0;i<n;i++){
        int tmp;
        std::cin>>tmp; 
        arr.push_back(tmp);
    }

    std::sort(arr.begin(),arr.end());

    int sum = 0;
    int pairs =0;
    int prev = -1;
    for (auto i : arr){
        if(prev != i){
            pairs += sum/2;
            sum = 0;            
        }
        sum+=1;
        prev = i;
    }
    pairs += sum/2;

    std::cout<<pairs<<std::endl;
    
}