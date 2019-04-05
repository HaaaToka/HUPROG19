#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if (x < y) x = y; }

struct BinCoeffPrimePower {
    vector<int> fact;        //(x!)_p
    vector<int> factinv;    //fact[x]^{-1} mod P

    void init(int maxN_, int p_, int q_) {
        assert(1 < p_ && 1 <= q_);
        p = p_, q = q_;
        P = p; for (int k = 1; k < q; ++k) P *= p;
        int maxN = min(max(0, maxN_), P - 1);

        fact.resize(maxN + 1);
        fact[0] = 1;
        for (int x = 1; x <= maxN; ++x) {
            fact[x] = x % p == 0 ? fact[x - 1] : mul(fact[x - 1], x);
        }
        factinv.resize(maxN + 1);
        factinv[maxN] = inverse(fact[maxN]);
        for (int x = maxN; x >= 1; --x) {
            factinv[x - 1] = x % p == 0 ? factinv[x] : mul(factinv[x], x);
        }
    }

    int getP() const { return P; }

    int nCr(int n, int r) const {
        if (r > n) return 0;
        assert(0 <= n && (n >= getP() || n < (int)fact.size()) && 0 <= r);

        int z = n - r;

        int e0 = 0;
        for (int u = n / p; u > 0; u /= p) e0 += u;
        for (int u = r / p; u > 0; u /= p) e0 -= u;
        for (int u = z / p; u > 0; u /= p) e0 -= u;

        int em = 0;
        for (int u = n / P; u > 0; u /= p) em += u;
        for (int u = r / P; u > 0; u /= p) em -= u;
        for (int u = z / P; u > 0; u /= p) em -= u;

        int prod = 1;
        while (n > 0) {
            prod = mul(prod, fact[n % P]);
            prod = mul(prod, factinv[r % P]);
            prod = mul(prod, factinv[z % P]);
            n /= p, r /= p, z /= p;
        }

        if (!(p == 2 && q >= 3) && em % 2 != 0)
            prod = P - prod;

        for (int i = 0; i < e0 && i < q; ++i)
            prod = mul(prod, p);

        return prod;
    }

private:
    int mul(int x, int y) const { return (long long)x * y % P; }

    int inverse(signed a) const {
        a %= P;
        if (a < 0) a += P;
        signed b = P, u = 1, v = 0;
        while (b) {
            signed t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        if (u < 0) u += P;
        return u;
    }

    int p, q, P;
};

struct BinCoeff {
    void init(int maxN, const vector<pair<int, int>> &factors) {
        bcpps.resize(factors.size());
        crtCoeffs.resize(factors.size());
        int M = 1;
        for (int i = 0; i < (int)factors.size(); ++i) {
            bcpps[i].init(maxN, factors[i].first, factors[i].second);
            int P = bcpps[i].getP();
            int t, g;
            t = exgcd(M % P, P, g);
            assert(g == 1);
            crtCoeffs[i] = t;
            M *= P;
        }
    }

    int nCr(int n, int r) const {
        int A = 0, M = 1;
        for (int i = 0; i < (int)crtCoeffs.size(); ++i) {
            int P = bcpps[i].getP();
            int a = bcpps[i].nCr(n, r);
            int d = (a - A) % P;
            int h = (long long)d * crtCoeffs[i] % P;
            if (h < 0) h += P;
            A += M * h;
            M *= P;
        }
        return A;
    }

private:
    vector<BinCoeffPrimePower> bcpps;
    vector<int> crtCoeffs;

    static int exgcd(int a, int b, int &g) {
        int u = 1, v = 0;
        while (b) {
            int t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        g = a;
        return u;
    }
};


vector<bool> isprime;
vector<int> primes;
void sieve(int n) {
    if ((int)isprime.size() >= n + 1) return;
    isprime.assign(n + 1, true);
    isprime[0] = isprime[1] = false;
    int sqrtn = (int)(sqrt(n * 1.) + .5);
    for (int i = 2; i <= sqrtn; i++) if (isprime[i]) {
        for (int j = i * i; j <= n; j += i)
            isprime[j] = false;
    }
    primes.clear();
    for (int i = 2; i <= n; i++) if (isprime[i])
        primes.push_back(i);
}

typedef int FactorsInt;
typedef vector<pair<FactorsInt, int> > Factors;
void primeFactors(FactorsInt x, Factors &out_v) {
    out_v.clear();
    int sqrtx = (int)(sqrt(x*1.) + 10.5);
    sieve(sqrtx);
    for (vector<int>::const_iterator p = primes.begin(); p != primes.end(); ++p) {
        if (*p > sqrtx) break;
        if (x % *p == 0) {
            int t = 1;
            x /= *p;
            while (x % *p == 0) {
                t++;
                x /= *p;
            }
            out_v.push_back(make_pair(*p, t));
        }
    }
    if (x != 1) out_v.push_back(make_pair(x, 1));
}

struct GModInt {
    static int Mod;
    unsigned x;
    GModInt() : x(0) {}
    GModInt(signed sig) { int sigt = sig % Mod; if (sigt < 0) sigt += Mod; x = sigt; }
    GModInt(signed long long sig) { int sigt = sig % Mod; if (sigt < 0) sigt += Mod; x = sigt; }
    int get() const { return (int)x; }

    GModInt &operator+=(GModInt that) { if ((x += that.x) >= (unsigned)Mod) x -= Mod; return *this; }
    GModInt &operator-=(GModInt that) { if ((x += Mod - that.x) >= (unsigned)Mod) x -= Mod; return *this; }
    GModInt &operator*=(GModInt that) { x = (unsigned long long)x * that.x % Mod; return *this; }

    GModInt operator+(GModInt that) const { return GModInt(*this) += that; }
    GModInt operator-(GModInt that) const { return GModInt(*this) -= that; }
    GModInt operator*(GModInt that) const { return GModInt(*this) *= that; }
};
int GModInt::Mod = 0;
typedef GModInt mint;

int main() {
    sieve(32000);
    BinCoeff bc;

    for (int ii = 0; ii < 5; ++ii) {
        int N; int M;
        scanf("%d%d", &N, &M);
        int S; int F;
        scanf("%d%d", &S, &F);
        int MOD;
        scanf("%d", &MOD);
        mint::Mod = MOD;
        {
            Factors factors;
            primeFactors(MOD, factors);
            bc.init(N + M, factors);
        }
        vector<pair<int, int> > carrots(S);
        for (int i = 0; i < S; ++i) {
            scanf("%d%d", &carrots[i].first, &carrots[i].second);
            --carrots[i].first, --carrots[i].second;
        }
        sort(all(carrots));
        carrots.insert(carrots.begin(), make_pair(0, 1));
        carrots.insert(carrots.begin() + 1, make_pair(1, 0));
        carrots.insert(carrots.end(), make_pair(N - 2, M - 1));
        carrots.insert(carrots.end(), make_pair(N - 1, M - 2));
        vector<vector<mint>> combs(S + 4, vector<mint>(S + 4));
        rep(i, S + 4) reu(j, i + 1, S + 4) {
            int x = carrots[j].first - carrots[i].first;
            int y = carrots[j].second - carrots[i].second;
            if (x >= 0 && y >= 0)
                combs[i][j] = bc.nCr(x + y, x);
        }

        vector<vector<mint>> ways(S + 4, vector<mint>(S + 4));
        rep(i, S + 4) {
            ways[i][i] = 1;
            reu(j, i + 1, S + 4) {
                mint x = combs[i][j];
                reu(k, i + 1, j)
                    x -= ways[i][k] * combs[k][j];
                ways[i][j] = x;
            }
        }
        vector<vector<mint>> dp1(S + 4, vector<mint>(F + 2)), dp2 = dp1;
        dp1[0][0] = dp2[1][0] = 1;
        rep(i, S + 4) reu(k, i + 1, S + 4) {
            mint mul = ways[i][k];
            if (mul.x == 0) continue;
            rer(j, 0, F) {
                dp1[k][j + 1] += dp1[i][j] * mul;
                dp2[k][j + 1] += dp2[i][j] * mul;
            }
        }
        mint ans;
        rer(d, 0, F) rer(e, 0, F - d) {
            mint a = dp1[S + 2][d + 1];
            mint b = dp1[S + 3][d + 1];
            mint c = dp2[S + 2][e + 1];
            mint d = dp2[S + 3][e + 1];
            mint det = a * d - b * c;
            ans += det;
        }
        printf("%d\n", ans.get());
    }
    return 0;
}
