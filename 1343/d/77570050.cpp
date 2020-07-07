// D div 3 solution
// for full go to bit.ly/cfdiv23boostlive
 
#include<bits/stdc++.h>
using namespace std;
 
#define FOR(a, b, c) for(int a = b; a <= c; ++a)
#define FORW(a, b, c) for(int a = b; a >= c; --a)
#define fi first
#define se second
#define pb push_back
#define int long long
 
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
const int N = 6e5 + 100;
const int maxN = 1e16;
const int oo = 1e18;
const int mod  = 1e9 + 7;
 
int n, k;
int cnt[N];
int maxn[N], minn[N];
int a[N];
 
signed main()  {
//   freopen("test.inp", "r", stdin);
//    freopen("spm.out", "w", stdout);
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int t; cin >> t;
    while(t --) {
        cin >> n >> k;
        FOR(i, 1, n) cin >> a[i];
        FOR(i, 1, n / 2) {
            maxn[i] = max(a[i], a[n - i + 1]) + k, cnt[ a[i] + a[n - i + 1] ] ++;
            minn[i] = min(a[i], a[n - i + 1]);
        }
        sort(maxn + 1, maxn + n / 2 + 1);
        sort(minn + 1, minn + n / 2 + 1);
        int ans = oo;
        FOR(i, 1, 2 * k)  {
            int val = i;
            int pos1 = lower_bound(maxn + 1, maxn + n / 2 + 1, val) - maxn - 1;
            int pos2 = lower_bound(minn + 1, minn + n / 2 + 1, val) - minn;
 
            pos2 = n / 2 - pos2 + 1;
 
            int tmp = (pos1 + pos2) * 2 + (n / 2 - pos1 - pos2) - cnt[ val ];
            ans = min(ans, tmp);
        }
        FOR(i, 1, n / 2) cnt[ a[i] + a[n - i + 1] ] --;
        cout << ans << '\n';
    }
}