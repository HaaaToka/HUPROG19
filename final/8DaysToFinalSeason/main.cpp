#define ONLINE_JUDGE
#include<bits/stdc++.h>

#define HEAP priority_queue
#define rep(i, n) for(int i = 0, _end_ = (n); i < _end_; ++i)
#define per(i, n) for(int i = (n) - 1; i >= 0 ; --i)
#define forn(i, l, r) for(int i = (l), _end_ = (r); i <= _end_; ++i)
#define nrof(i, r, l) for(int i = (r), _end_ = (l); i >= _end_; --i)
#define FOR(a, b) for(auto (a): (b))
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define X first
#define Y second
#define eps 1e-6
#define pi 3.1415926535897932384626433832795
#define SZ(x) (int)x.size()
#define ALL(x) x.begin(), x.end()
#define FILL(a, b) memset((a), (b), sizeof((a)))
#define MCPY(a, b) memcpy((a), (b), sizeof((b)))

using namespace std;

typedef long long LL;
typedef double flt;
typedef vector<int> vi;
typedef vector<LL> vl;
typedef pair<int,int> pii;
typedef pair<int,LL> pil;
typedef pair<LL,int> pli;
typedef pair<LL,LL> pll;
typedef vector<pil> vil;
typedef vector<pii> vii;
typedef vector<pli> vli;
typedef vector<pll> vll;

const int iinf = 1e9 + 7;
const int oo = 0x3f3f3f3f;
const LL linf = 1ll << 60;
const flt dinf = 1e60;

template <typename T>
inline void scf(T &x)
{
    bool f = 0; x = 0; char c = getchar();
    while((c < '0' || c > '9') && c != '-') c = getchar();
    if(c == '-') { f = 1; c = getchar(); }
    while(c >= '0' && c <= '9') { x = x * 10 + c - '0'; c = getchar(); }
    if(f) x = -x; return;
}
template <typename T1, typename T2>
void scf(T1 &x, T2 &y) { scf(x); return scf(y); }
template <typename T1, typename T2, typename T3>
void scf(T1 &x, T2 &y, T3 &z) { scf(x); scf(y); return scf(z); }
template <typename T1, typename T2, typename T3, typename T4>
void scf(T1 &x, T2 &y, T3 &z, T4 &w) { scf(x); scf(y); scf(z); return scf(w); }

inline char mygetchar(){ char c = getchar(); while(c == ' ' || c == '\n') c = getchar(); return c; }

template <typename T> inline bool chkmax(T &x, const T &y){ return y > x ? x = y, 1 : 0; }
template <typename T> inline bool chkmin(T &x, const T &y){ return y < x ? x = y, 1 : 0; }

#ifdef ONLINE_JUDGE
#define debug(...) ;
#else
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define DEBUG
#endif

//---------------------------------------------------------head----------------------------------------------------

void judge()
{
//    freopen("grid.in", "r", stdin);
//    freopen("grid.out", "w", stdout);
    return;
}

const int maxw = 2e5 + 100;

const int maxn = 233;

const int maxm = 12;

int H, W, n, m, K, Mod;
int p[maxm], q[maxm], x[maxn], y[maxn], mod[maxm], id[maxn];
pii fac[maxw][maxm];
int dp[maxn][maxn], f1[maxn][maxn], f2[maxn][maxn], f3[maxn][maxn], f4[maxn][maxn], pd[maxn][maxn];
bool flag[maxn];

#ifdef DEBUG
int CC[200][200];
#endif

inline void ext_gcd(LL a, LL &x, LL b, LL &y)
{
    if(!b)
    {
        x = 1; y = 0;
        return;
    }
    ext_gcd(b, y, a % b, x);
    y -= (a / b) * x;
    return;
}

inline int inv(int n, int mod)
{
    LL x, y;
    ext_gcd(n, x, mod, y);
    return ((x % mod) + mod) % mod;
}

inline int pow_mod(int x, int n, const int &mod)
{
    int y = 1;
    while(n)
    {
        if(n & 1) y = 1ll * y * x % mod;
        x = 1ll * x * x % mod;
        n >>= 1;
    }
    return y;
}

void get_mod()
{
    int mod; scf(mod);
    Mod = mod;
    m = 0;
    for(int i = 2; i * i <= mod; ++i) if(mod % i == 0)
    {
        p[m] = i; q[m] = 0; ::mod[m] = mod;
        while(mod % i == 0) mod /= i, ++q[m];
        ::mod[m] /= mod;
        ++m;
    }
    if(mod > 1) p[m] = mod, q[m] = 1, ::mod[m] = mod, ++m;
    return;
}

void pre()
{
    rep(m, ::m)
    {
        fac[0][m] = mp(1, 0);
        forn(i, 1, H + W)
        {
            int x = i, y = 0;
            while(x % p[m] == 0) x /= p[m], ++y;
            fac[i][m] = mp(1ll * fac[i - 1][m].X * x % mod[m], fac[i - 1][m].Y + y);
        }
    }
    return;
}

inline bool cmp(const int &i, const int &j)
{
    return (x[i] == x[j]) ? ((y[i] == y[j]) ? (i < j) : (y[i] > y[j])) : (x[i] > x[j]);
}

inline int C(int N, int M)
{
    if(N < M || N < 0 || M < 0) return 0;
    int ret = 0;
    rep(i, m)
    {
        int r  = 1ll * fac[N][i].X * inv(fac[M][i].X, mod[i]) % mod[i] * inv(fac[N - M][i].X, mod[i]) % mod[i];
        int y = fac[N][i].Y - fac[M][i].Y - fac[N - M][i].Y;
        r = 1ll * r * pow_mod(p[i], y, mod[i]) % mod[i];
        ret = (1ll * Mod / mod[i] * inv(Mod / mod[i], mod[i]) % Mod * r % Mod + ret) % Mod;
    }
#ifdef DEBUG
//    debug("asserting...\n");
    assert(CC[N][M] == ret);
#endif
    return ret;
}

void work(int S, int T, int (&dp)[maxn][maxn])
{
    memset(dp, 0, sizeof dp);
//    debug("%d\n", flag[id[T]]);
    dp[T][flag[id[T]]] = 1;
    int tmp;
    forn(i, T, S - 1) forn(j, 0, K) if(tmp = dp[i][j]) forn(k, i + 1, S) dp[k][j + flag[id[k]]] = (1ll * tmp * ::dp[k][i] + dp[k][j + flag[id[k]]]) % Mod;
    return;
}

void solve()
{
    memset(dp, 0, sizeof dp);
    memset(pd, 0, sizeof pd);
    scf(H, W, n, K);
    get_mod();
    pre();
#ifdef DEBUG
    CC[0][0] = 1;
    forn(i, 1, 199)
    {
        CC[i][0] = CC[i][i] = 1;
        forn(j, 1, i - 1) CC[i][j] = (CC[i - 1][j] + CC[i - 1][j - 1]) % Mod;
    }
#endif
    bool f1, f2, f3, f4; f1 = f2 = f3 = f4 = 0;
    memset(flag, 0, sizeof flag);
    forn(i, 1, n)
    {
        scf(x[i], y[i]);
        f1 |= (x[i] == 1 && y[i] == 2);
        f2 |= (x[i] == 2 && y[i] == 1);
        f3 |= (x[i] == H && y[i] == W - 1);
        f4 |= (x[i] == H - 1 && y[i] == W);
        flag[i] = 1;
    }
    if(!f1)
    {
        ++n, x[n] = 1, y[n] = 2;
        f2 |= (x[n] == 2 && y[n] == 1);
        f3 |= (x[n] == H && y[n] == W - 1);
        f4 |= (x[n] == H - 1 && y[n] == W);
    }
    if(!f2)
    {
        ++n, x[n] = 2, y[n] = 1;
        f3 |= (x[n] == H && y[n] == W - 1);
        f4 |= (x[n] == H - 1 && y[n] == W);
    }
    if(!f3)
    {
        ++n; x[n] = H, y[n] = W - 1;
        f4 |= (x[n] == H - 1 && y[n] == W);
    }
    if(!f4) ++n, x[n] = H - 1, y[n] = W;
    forn(i, 1, n) id[i] = i;
    sort(id + 1, id + n + 1, cmp);
//    forn(i, 1, n) printf("%d %d\n", x[id[i]], y[id[i]]);
    forn(I, 1, n) nrof(J, I - 1, 1)
    {
        int i = id[I], j = id[J];
        pd[I][J] = (x[i] <= x[j] && y[i] <= y[j]) ? C(x[j] - x[i] + y[j] - y[i], x[j] - x[i]) : 0;
    }
    forn(I, 1, n) nrof(J, I - 1, 1)
    {
        dp[I][J] = pd[I][J];
        forn(K, J + 1, I - 1) dp[I][J] = ((-1ll * dp[I][K] * pd[K][J] + dp[I][J]) % Mod + Mod) % Mod;
//        if(dp[I][J]) debug("dp[%d][%d] = %d\n", I, J, dp[I][J]);
    }
    int i1, i2, i3, i4;
    forn(I, 1, n)
    {
        int i = id[I];
        if(x[i] == 1 && y[i] == 2) i1 = I;
        if(x[i] == 2 && y[i] == 1) i2 = I;
        if(x[i] == H && y[i] == W - 1) i3 = I;
        if(x[i] == H - 1 && y[i] == W) i4 = I;
    }
    debug("%d %d %d %d\n", i1, i2, i3, i4);
    work(i1, i3, ::f1);
    work(i1, i4, ::f2);
    work(i2, i3, ::f3);
    work(i2, i4, ::f4);
    int ans = 0;
    forn(i, 0, K) forn(j, 0, K - i) ans = ((1ll * ::f2[i1][i] * ::f3[i2][j] - 1ll * ::f1[i1][i] * ::f4[i2][j] + ans) % Mod + Mod) % Mod;
    printf("%d\n", ans);
    return;
}

int main()
{
#ifdef ONLINE_JUDGE
    judge();
#endif
    int T=5;
    forn(tc, 1, T) solve();
    return 0;
}