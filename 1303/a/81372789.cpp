/*
himanshu18038
*/
#include<bits/stdc++.h>
using namespace std;

#define fastio() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;

#define pb push_back
#define mp make_pair
#define fi first 
#define se second
#define unordered_map u_map
#define unordered_set u_set

#define rep(i,a,b) for(int i=int(a);i<int(b);i++)
#define repn(i,a,b) for(int i=int(a);i>int(b);i--)
#define repeach(a, b) for (auto&(a) : (b))
#define repg(i,a,b,g) for(int i=int(a);i<int(b);i+=g)

#define take_input(v) repeach(i,v){cin>>i;}
#define show_list(v) repeach(i,v){cout<<i<<" ";}

#define value(x) cerr << "The value of " << #x << " is " << x << "\n"

#define len(v) (int)v.size()
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))


#define mod 1e9+7
#define PI 3.141592653589793238463
#define INF 1000000000000000005LL

/*int gcd(int a, int b){ 
	if(a==0)
		return b; 
	return gcd(b%a, a); 
}*/

void solve(){
	string s;
	cin>>s;
	int n=s.length(), x=-1, y=n-1, ans=0;
	rep(i,0,n){
		if(s[i]=='0'){
			x=i;
		}
		else{
			break;
		}
	}
	repn(i,n-1,-1){
		if(s[i]=='0'){
			y=i;
		}
		else{
			break;
		}	
	}
	//cout<<x<<" "<<y;
	rep(i,x+1,y){
		if(s[i]=='0'){
			ans+=1;
		}
	}
	cout<<ans<<"\n";
}

signed main(){
	fastio();
	int t=1;
	cin>>t;
	while(t--){
		solve();
	}
	return 0;
}