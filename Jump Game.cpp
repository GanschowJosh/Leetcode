#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int length = nums.size();
        int min = length - 1;
        for(int i = length-1; i >= 0; i--) {
            if(nums[i] + i >= min) min = i;
        }
        return (min == 0);
    }
};