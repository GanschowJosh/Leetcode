#include <bits/stdc++.h>
using namespace std;

int hindex(vector<int>& citations) {
    sort(citations.begin(), citations.end());
    for(int i = 0; i < citations.size(); i++) {
        if (citations.size() - i <= citations[i]) {
            return citations.size() - i;
        }
    }
    return citations.size();
}

int main() {
    vector<int> citations = {3, 0, 6, 1, 5};
    cout << hindex(citations) << endl;
}