#include<bits/stdc++.h>

using namespace std;

int arr[1001];

int main()
{
	int n, m;
	int x;
	cin >> n >> m;
	for (int i = 0; i < m; i++)cin >> x, arr[x] = 1;

	int ans = (int)1e9;
	for (int i = 1; i <= 1000; i++) {
		if (arr[i] == 1)continue;
		for (int j = i; j <= 1000; j++) {
			if (arr[j] == 1)continue;
			for (int k = j; k <= 1001; k++) {
				if (arr[k] == 1)continue;
				ans = min(ans, abs(n - i * j * k));
			}
		}
	}
	cout << ans;
	return 0;
}