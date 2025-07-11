#include <bits/stdc++.h>
#include <iostream>
using namespace std;


//O(n^2) no good
// int maxProfit(vector<int>& prices) {
//     int max = 0;
//     for(auto i = 0; i < prices.size(); i++) {
//         for(auto it = prices.begin() + i; it < prices.end(); it++) {
//             cout << prices[i] << " " << *it << endl;
//             auto diff = *it - prices[i];
//             if(diff > max) max = diff;
//         }
//     }
//     return max;
// }

//O()

int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX;
    int maxProfit = 0;
    for(int i = 0; i < prices.size(); i++) {
        if(prices[i] < minPrice) minPrice = prices[i];
        else if(prices[i] - minPrice > maxProfit) maxProfit = prices[i] - minPrice;
    }
    return maxProfit;
}

int main() {
    vector<int> p = {7, 6, 4, 3, 1};
    cout << maxProfit(p) << endl;
    return 0;
}