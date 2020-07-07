#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define REP(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define vi vector<int>
#define vll vector<ll>
#define vvi vector < vi >
#define pii pair<int,int>
#define pll pair<long long, long long>
#define modulo 1000000007;
#define inf 1000000000000000001;
#define all(c) c.begin(),c.end()
#define mp(x,y) make_pair(x,y)
#define mem(a,val) memset(a,val,sizeof(a))
#define eb emplace_back
#define f first
#define s second
#define error(args...) { string _s = #args; replace(_s.begin(), _s.end(), ',', ' '); stringstream _ss(_s); istream_iterator<string> _it(_ss); err(_it, args); }

void err(istream_iterator<string> it) {}
template<typename T, typename... Args>
void err(istream_iterator<string> it, T a, Args... args) {
	cerr << *it << " = " << a << endl;
	err(++it, args...);
}

// functions
ll power(ll x, ll y, ll mod = 2e18){ ll ans = 1;x %= mod;while(y){if(y&1)ans = (x * ans) % mod;x = (x * x) % mod;y >>= 1;}return ans;}
ll modInverse(ll a, ll m){ll m0 = m;ll y = 0, x = 1;if (m == 1) return 0;while (a > 1){ ll q = a / m;ll t = m;m = a % m,a = t;t = y;y = x - q * y;x = t;}if(x < 0) x += m0;return x;} 
ll gcdext(ll a,ll b,ll *x = 0, ll *y = 0){if(a == 0){*x = 0;*y = 1;return b;}ll x1,y1;ll gcd1 = gcdext(b%a,a,&x1,&y1);*x = y1 - (b/a)*x1;*y = x1;return gcd1;}
mt19937 mrand(random_device{}());
int rnd(int x) { return mrand() % x;} 
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int test;
	cin>>test;
	while(test--){
		ll n, k;
		cin>>n>>k;
		vll arr(n);
		REP(i,0,n)	cin>>arr[i];

		bool peaks[n];
		mem(peaks, false);
		REP(i,1,n-1){
			if(arr[i-1] < arr[i] && arr[i] > arr[i+1])
				peaks[i] = true;
		}
		vector<pair<ll,ll>> maxPeaks;
		ll curPeak = 0;
		REP(i,1,k-1){
			if(peaks[i])
				curPeak++;
		}
		maxPeaks.eb(mp(curPeak,0));
		REP(i,1,n-k+1){
			if(peaks[i])
				curPeak--;
			if(peaks[i+k-2])
				curPeak++;
			maxPeaks.eb(mp(curPeak,i));
		}
		sort(all(maxPeaks), [](pll& a, pll& b){
			if(a.f == b.f)
				return a.s < b.s;
			else
				return a.f > b.f;
		});
		cout<<maxPeaks[0].f+1<<" "<<maxPeaks[0].s+1<<endl;
	}
	return 0;
}