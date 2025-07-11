#include <bits/stdc++.h>
#include <iostream>
using namespace std;

//naive approach
// int jump(vector<int>& nums) {
//     int mx, mi; // variables to keep track of max value and index of max value
//     int i = 0, start, counter = 0;
//     int sz = nums.size();
//     while(i < nums.size()) {
//         counter++;
//         if(nums.size() < 2) {
//             return 0;
//         }
//         if(i + nums[i] >= sz-1) { //current reaches end
//             return counter;
//         }
//         else { //current doesn't reach, choose largest of next i terms
//             mx = *(nums.begin() + i);
//             mi = i;
//             for(int j = i; j <= i + nums[i]; j++) {
//                 // cout << i << " " << j << nums[i] << endl;
//                 if(nums[j] >= mx) {
//                     mx = nums[j];
//                     mi = j;
//                 }
//             }
//             i = mi;
//         }
//         // cout << i << endl;
//     }
//     return counter;
// }


int jump(vector<int>& nums) {
    int n = nums.size();
    if(n < 2) return 0;
    int maxPosition = nums[0], maxSteps = nums[0];
    int jumps = 1;
    for(int i = 0; i < n; i++) {
        if(maxSteps < i) { //reached end of currently reachable window
            jumps++;
            maxSteps = maxPosition;
        }
        maxPosition = max(maxPosition, nums[i] + i);
    }
    return jumps;
}

int main() {

    vector<int> nums = {1, 2, 1, 1, 1};

    cout << jump(nums) << endl;
}