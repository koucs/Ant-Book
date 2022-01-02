#! env python
# -*- coding: utf-8 -*-

import heapq

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')


def main():
    N = int(input())  # vertex num
    R = int(input())  # edge num
    G = [[] * N for _ in range(N)]
    for _ in range(R):
        f, t, c = map(int, input().split())
        G[f].append([t, c])  # G[from_vertex][] = [to_vertex, cost]
        G[t].append([f, c])

    def solve(start: int):
        que = []
        dist = [INF for _ in range(N)]
        dist2 = [INF for _ in range(N)]
        dist[start] = 0
        heapq.heappush(que, (0, start))  # (distance, vertex index)

        while len(que) != 0:
            # print(f"dist: {dist}, dist2: {dist2}, que: {que}")
            p = heapq.heappop(que)
            d, from_vertex = p[0], p[1]
            if dist2[from_vertex] < p[0]:
                continue
            for i in range(len(G[from_vertex])):
                edge = G[from_vertex][i]
                d2 = d + edge[1]
                to_vertex = edge[0]

                # d2 (que top の distance(from_vertex) + edge の distance (from_vertex -> to_vertex)
                # が dist[to_vertex] よりも低い場合は最短経路になるのでswapしてqueにpush
                if d2 < dist[to_vertex]:
                    dist[to_vertex], d2 = d2, dist[to_vertex]
                    heapq.heappush(que, (dist[to_vertex], to_vertex))

                # d2がdist2[to_vertex]よりも低い場合はdist2を更新してqueにpush
                if dist[to_vertex] < d2 < dist2[to_vertex]:
                    dist2[to_vertex] = d2
                    heapq.heappush(que, (dist2[to_vertex], to_vertex))
        return dist2[N - 1]

    print(solve(0))
    return


if __name__ == '__main__':
    main()
