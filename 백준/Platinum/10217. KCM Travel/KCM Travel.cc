#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <limits>
#define pii pair<int, int>
#define INF numeric_limits<int>::max()
using namespace std;

struct node{
    int n, c, d;
    bool operator < (node &other){
        if(d == other.d) return c < other.c;
        return d < other.d;
    }
};
struct cmp{
    bool operator()(node &A, node &B){
        return A.d > B.d;
    }
};

int N, M, K;
int dist[101][10001];
bool visit[101][10001];
vector<node> adj[101];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T; cin >> T;

    while(T--){
        cin >> N >> M >> K;
        int mm = -1;
        for (int i = 0; i < K; i++){
            int prev, nxt, c, d; cin >> prev >> nxt >> c >> d;
            node temp = {nxt, c, d};
            adj[prev].push_back(temp);
            if(nxt == N) mm = min(mm, c);
        }
        for(int i = 1; i <= N; i++){
            fill(dist[i], dist[i]+10001, INF);
            sort(adj[i].begin(), adj[i].end());
        }
        for(int i = 1; i <= 10000; i++){
            visit[1][i] = true;
        }
        
        dist[1][0] = 0;

        priority_queue<node, vector<node>, cmp> pq;
        node temp = {1, 0, 0};
        pq.push(temp);
        
        while(!pq.empty()) {
            int curr, co, di;

            do{
                curr = pq.top().n;
                co = pq.top().c;
                di = pq.top().d;
                pq.pop();
            } while (!pq.empty() && visit[curr][co]);
            
            if (visit[curr][co]) break;
            visit[curr][co] = true;
            if (curr == N) break;
            if (dist[curr][co] < di) continue;

            for (auto nod: adj[curr]) {
                int nxt = nod.n, nx_co = nod.c, nx_di = nod.d;
                
                if (visit[nxt][nx_co]) continue;
                if (co + nx_co > M) continue;
                if (nxt != N && co + nx_co + mm > M) continue;

                if (di + nx_di < dist[nxt][co+nx_co]) {
                    for(int i = co+nx_co; i <= M; i++) 
                        if (dist[nxt][i] > di+nx_di) dist[nxt][i] = di+nx_di;
                        else break;
                    node temp = {nxt, co+nx_co, di+nx_di};
                    pq.push(temp);
                }
            }
        }
        int result = INF;
        for (int i = 1; i <= M; i++){
            result = min(dist[N][i], result);
        }
        if (result == INF) cout << "Poor KCM" << '\n';
        else cout << result << '\n';
    }
}