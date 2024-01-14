#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int n;
  cin >> n;
  vector<int> arr(n);
  
  for(int i = 0; i < n; i++) cin >> arr[i];
  sort(arr.begin(), arr.end());
  
  long long ans = 0;
  for(int i = 0; i < n-1; i++) {
    for(int j = i+1; j < n; j++) {
      int two;
      int idx;
      two = arr[i] + arr[j];
      idx = upper_bound(arr.begin()+j+1, arr.end(), -two) - lower_bound(arr.begin()+j+1, arr.end(), -two);
      ans += idx;
    }
  }
  cout << ans << "\n";
}
