#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,k,m;
    cin >> n >> m >>k;
    int t;
    //vector<int> sm;
    int sm[m+1];
    for(int i = 0; i<n-(k-1); i++){
        cin >> t;
        sm[i] = t;
    }
    int ix;
    int dumb = 10000;
    int arr[n];
    for(int i =0; i<n; i++){
        arr[i] = dumb;
    }
    for(int i = 0; i<k-1; i++){
        
        cin >> ix >> t;
        ix--;
        arr[ix] = t;
        int e = ix-k;
        while(e >=0){
            arr[e] = arr[e+k] - (sm[e+1] - sm[e]); 
            e -=k;
        }
        
        e = ix+k;
        while(e < n){
            arr[e] = arr[e-k] + (sm[e-k+1] - sm[e-k]); 
            e+=k;
        }
    }
    
    for(int ix = 0; ix<k; ix++){
        
        if (arr[ix] == dumb){
            
            int sum_til_k = 0;
            for(int i = 0; i<k;i++){
                sum_til_k+=arr[i];
            }
            sum_til_k-= dumb;
            arr[ix] = sm[0] - sum_til_k;
            int e = ix+k;
            while(e < n){
                arr[e] = arr[e-k] + (sm[e-k+1] - sm[e-k]); 
                e+=k;
            }
            break;
        }
    }
    for (int i = 0;i<n;i++){
        cout << arr[i] << " ";
    }
    return 0;
}
