class Solution {
  public:
    void reverseArray(vector<int> &arr) {
        reverse(arr, 0, arr.size()-1); 
    }
    void reverse(vector<int> & arr, int i, int j){
        if (i>=j) return;
        int temp = arr[i];
        arr[i] = arr[j]; 
        arr[j] = temp; 
        reverse(arr,i+1, j-1); 
    }
};
