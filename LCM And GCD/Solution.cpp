class Solution {
  public:
    vector<int> lcmAndGcd(int a, int b) {
        vector<int> answer = {lcm(a,b), gcd(a,b)};
        return answer; 
    }
    
    int gcd(int a, int b){
        if (b == 0){
            return a; 
        }
        if (b > a){
            int temp = a;
            a = b; 
            b = temp; 
        }
        return gcd(b, a%b);
    }
    
    int lcm(int a, int b){
        return abs(a*b)/gcd(a,b);
    }
};
