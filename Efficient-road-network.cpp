#define ll long long int
#define pb(x) push_back(x)
#define vi vector<int>
#include <bits/stdc++.h>
using namespace std;
// https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/ty4w8WJZ4sZSBNK5Q

bool BFS(vector<int> adj[], int src, int dest, int v, int pred[], int dist[])
{
    list<int> queue;
    bool visited[v];
    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        pred[i] = -1;
        dist[i] = INT_MAX;
    }
    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);
    while (!queue.empty())
    {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++)
        {
            int t = adj[u][i];
            if (visited[t] == false)
            {
                visited[t] = true;
                dist[t] = dist[u] + 1;
                pred[t] = u;
                queue.push_back(t);
                if (t == dest)
                    return true;
            }
        }
    }
    return false;
}

bool efficientRoadNetwork(int n, vector<vector<int>> roads)
{
    vector<int> Adj[n];
    for (auto x : roads)
    {
        Adj[x[0]].push_back(x[1]);
        Adj[x[1]].push_back(x[0]);
    }
    int predecessor[n], distance[n];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i != j)
            {
                BFS(Adj, i, j, n, predecessor, distance);
                vector<int> path;
                int crawl = j;
                path.push_back(crawl);
                while (predecessor[crawl] != -1)
                {
                    path.push_back(predecessor[crawl]);
                    crawl = predecessor[crawl];
                }
                if (distance[j] > 2)
                {
                    return false;
                }
            }
        }
    }
    return true;
}

int main(void)
{
    int n = 6;
    // vector<vector<int>> roads = {{3, 0}, {0, 4}, {5, 0}, {2, 1}, {1, 4}, {2, 3}, {5, 2}};
    vector<vector<int>> roads = {{0, 4}, {5, 0}, {2, 1}, {1, 4}, {2, 3}, {5, 2}};
    cout << efficientRoadNetwork(n, roads);
}