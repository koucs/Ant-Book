#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')


def main():
    V = int(input())
    E = int(input())
    cost = [[INF] * V for _ in range(V)]
    for _ in range(E):
        f, t, c = map(int, input().split())
        cost[f][t] = c
        cost[t][f] = c

    prev = [-1] * V #

    def dijkstra(start: int):
        d = [INF for _ in range(V)]
        used = [False] * V
        d[start] = 0
        while True:
            v = -1
            # 'v' will store the minimum distance in d[] AND used[u] == False
            for u in range(V):
                if not used[u] and (v == -1 or d[u] < d[v]):
                    v = u
            if v == -1:
                break

            used[v] = True

            for u in range(V):
                # Update a cost of d[u] if v -> u is lower than current d[u]
                if d[u] > d[v] + cost[v][u]:
                    d[u] = d[v] + cost[v][u]
                    prev[u] = v

        return d

    def get_path(goal: int):
        path = []
        while goal != -1:
            path.append(goal)
            goal = prev[goal]
        path.reverse()
        return path

    print(dijkstra(0))
    print(get_path(V - 1))
    return


if __name__ == '__main__':
    main()
