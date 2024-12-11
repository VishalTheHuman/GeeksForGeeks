class Solution {
  public:
    // Function to count the frequency of all elements from 1 to N in the array.
    vector<int> frequencyCount(vector<int>& arr) {
        vector<int> store(arr.size()); 
        for(int x : arr){
            store[x-1]++;
        }
        return store; 
    }
};
