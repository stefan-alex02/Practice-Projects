import heapq


def dijkstra(n, m, s, e, b, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append((v, max(b[u - 1], b[v - 1])))
        graph[v].append((u, max(b[u - 1], b[v - 1])))

    dist = [float('inf')] * (n + 1)
    dist[s] = b[s - 1]
    pq = [(b[s - 1], s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > max(d, w):
                dist[v] = max(d, w)
                heapq.heappush(pq, (dist[v], v))

    return dist[e] if dist[e] != float('inf') else -1


def main():
    n, m, s, e = map(int, input().split())
    b = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(dijkstra(n, m, s, e, b, edges))


if __name__ == '__main__':
    main()
