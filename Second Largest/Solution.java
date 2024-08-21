

//User function Template for Java

class Solution {
    int print2largest(int arr[], int n) {
        int first,second;
        if(arr[0]>arr[1]){
            first=arr[0];
            second=arr[1];
        }
        else if(arr[1]>arr[0]){
            second=arr[0];
            first=arr[1];
        }else{
            first =arr[0];
            second =-1;
        }
        for(int i=2;i<n;i++){
            if(arr[i]>first){
                second=first;
                first=arr[i];
            }
            else if(arr[i]>second && arr[i]!=first){
                second=arr[i];
            }
        }
        return second;
    }
}

