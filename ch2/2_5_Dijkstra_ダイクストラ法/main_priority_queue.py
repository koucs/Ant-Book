#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')


def main():
    V = int(input())
    E = int(input())
    G = [[] * V for _ in range(V)]
    for _ in range(E):
        f, t, c = map(int,input().split())
        G[f].append([t, c]) # G[from_vertex][] = [to_vertex, cost]
        G[t].append([f, c])

    def dijkstra(start: int):
        que = []
        d = [INF for _ in range(V)]
        d[start] = 0
        heapq.heappush(que, (0, start)) # (distance, vertex index)

        while len(que) != 0:
            print(f"d: {d}, que: {que}")
            p = heapq.heappop(que)
            from_vertex = p[1]
            if d[from_vertex] < p[0]:
                continue
            for i in range(len(G[from_vertex])):
                edge = G[from_vertex][i]
                to_vertex = edge[0]
                if d[to_vertex] > d[from_vertex] + edge[1]:
                    d[to_vertex] = d[from_vertex] + edge[1]
                    heapq.heappush(que, (d[to_vertex], to_vertex))
        return d

    print(dijkstra(0))
    return


if __name__ == '__main__':
    main()
