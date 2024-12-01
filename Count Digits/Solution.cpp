class Solution {
  public:
    // Function to count the number of digits in n that evenly divide n
    int evenlyDivides(int n) {
        int count = 0;
        int num = n; 
        while (n>0){
            int val = n%10; 
            if (val!=0){
                if (num%val == 0){
                    count++; 
                }
            }
            n/=10; 
        }
        return count; 
    }
};
