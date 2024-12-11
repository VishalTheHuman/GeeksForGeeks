// User function Template for C++
class Solution {
  public:
    vector<long long> store; 
    long long base = 1, start = 1, limit ; 
    
    vector<long long> factorialNumbers(long long n) {
        limit = n;
        factorial();
        return store; 
    }
    
    void factorial(){
        if(base > limit) return;
        store.push_back(base); 
        start++; 
        base*=start; 
        factorial(); 
    }
};
