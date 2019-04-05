#include<bits/stdc++.h>
#define N 800005
#define ll long long
#define int long long
using namespace std;
int head[N/2],dfn[N],ed[N],son[N],heavyson[N],depth[N],father[N];
int n,T,s,p,x,y,Q,r,t,rr,kk,tim1=0,top[N];ll ee[N<<2],dp[N<<2];
struct Tree{int nxt,to;}e[N];
inline void link(int x,int y){e[++kk].nxt=head[x];e[kk].to=y;head[x]=kk;}
inline ll maxx(ll x,ll y){if(x<y)return y;return x;}
void dfs1(int u,int fa){
	son[u]=1;dfn[u]=++tim1;heavyson[u]=0;
	for (int i=head[u];i;i=e[i].nxt){
		int v=e[i].to;
		if (v==fa) continue;
		father[v]=u;depth[v]=depth[u]+1;
		dfs1(v,u);
		son[u]+=son[v];
		if (!heavyson[u]||son[v]>son[heavyson[u]]) heavyson[u]=v;
	}
	ed[u]=tim1;
}
void dfs2(int u,int first){
	top[u]=first;
	if (!heavyson[u]) return;
	dfs2(heavyson[u],first);
	for (int i=head[u];i;i=e[i].nxt){
		int v=e[i].to;
		if (v==father[u]||v==heavyson[u]) continue;
		dfs2(v,v);
	}
}
inline int lca(int x,int y){
	while (top[x]!=top[y]){
		if (depth[top[x]]<depth[top[y]]) swap(x,y);
		x=father[top[x]];
	}
	if (depth[x]<depth[y]) return x;return y;
}
void build(int k,int l,int r){
	dp[k]=0;ee[k]=0;
	if (l==r){if(l==dfn[s])dp[k]=p;return;}
	int mid=(l+r)>>1;
	build(k*2,l,mid);build(k*2+1,mid+1,r);
	dp[k]=maxx(dp[k*2],dp[k*2+1]);
}
inline void maintain(int k,int l,int r){
	if (l==r) return;
	ee[k*2]=maxx(ee[k*2],ee[k]);
	ee[k*2+1]=maxx(ee[k*2+1],ee[k]);
	dp[k*2]=maxx(dp[k*2],ee[k]);
	dp[k*2+1]=maxx(dp[k*2+1],ee[k]);
	ee[k]=0;
}
void update(int k,int l,int r,int x,int y,ll z){
	if (x>y||z<ee[k]) return;
	maintain(k,l,r);
	if (x<=l&&y>=r){dp[k]=maxx(dp[k],z);ee[k]=maxx(ee[k],z);return;}
	int mid=(l+r)>>1;
	if (y<=mid) update(k*2,l,mid,x,y,z);
	else if (x>mid) update(k*2+1,mid+1,r,x,y,z);
	else update(k*2,l,mid,x,mid,z),update(k*2+1,mid+1,r,mid+1,y,z);
	dp[k]=maxx(dp[k*2],dp[k*2+1]);
}
ll query(int k,int l,int r,int x,int y){
	if (x>y) return 0;
	maintain(k,l,r);
	if (x<=l&&y>=r) return dp[k];
	int mid=(l+r)>>1;
	if (y<=mid) return query(k*2,l,mid,x,y);
	else if (x>mid) return query(k*2+1,mid+1,r,x,y);
	else return maxx(query(k*2,l,mid,x,mid),query(k*2+1,mid+1,r,mid+1,y));
}
inline bool in(int x,int y){if(dfn[x]<=dfn[y]&&ed[x]>=dfn[y])return 1;return 0;}
inline int gt(int x,int y){
	if (in(heavyson[x],y)) return heavyson[x];
	while (father[top[y]]!=x) y=father[top[y]];
	return top[y];
}
inline int read(){
	char ch=getchar();int f=1,w=0;
	for (;ch<'0'||ch>'9';ch=getchar()) if (ch=='-') f=-1;
	for (;ch>='0'&&ch<='9';ch=getchar()) w=w*10+ch-'0';
	return w*f;
}
signed main(){
	T=1;
	while (T--){
		memset(head,0,sizeof(head));kk=0;tim1=0;
		//scanf("%lld%lld%lld",&n,&s,&p);
		n=read();s=read();p=read();
		for (int i=1;i<n;i++){
			//scanf("%lld%lld",&x,&y);
			x=read();y=read();
			link(x,y);link(y,x);
		}
		dfs1(1,-1);dfs2(1,1);
		build(1,1,n);
		//scanf("%lld",&Q);
		Q=read();
		while (Q--){
			//scanf("%lld%lld%lld%lld",&x,&y,&rr,&t);
			x=read();y=read();rr=read();t=read();
			int LCA=lca(x,y);
			if (y==LCA) swap(x,y);
			if (LCA==x){
				int l=dfn[y];int r=ed[y];
				ll tmp1=query(1,1,n,l,r);
				x=gt(x,y);
				int L1=1;int R1=dfn[x]-1;
				int L2=ed[x]+1;int R2=n;
				ll tmp2=maxx(query(1,1,n,L1,R1),query(1,1,n,L2,R2));
				if (tmp1>rr){update(1,1,n,L1,R1,tmp1+t),update(1,1,n,L2,R2,tmp1+t);}
				if (tmp2>rr) update(1,1,n,l,r,tmp2+t);
			}
			else {
				int l=dfn[x];int r=ed[x];
				int L=dfn[y];int R=ed[y];
				ll tmp1=query(1,1,n,l,r);
				ll tmp2=query(1,1,n,L,R);
				if (tmp1>rr) update(1,1,n,L,R,tmp1+t);
				if (tmp2>rr) update(1,1,n,l,r,tmp2+t);
			}
		}
		printf("%lld\n",dp[1]);
	}
	return 0;
}