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

    def prim():
        min_cost = [INF] * V
        used = [False] * V
        min_cost[0] = 0
        ans = 0

        while True:
            v = -1
            for u in range(V):
                if not used[u] and (v == -1 or min_cost[u] < min_cost[v]):
                    v = u

            if v == -1:
                break

            used[v] = True
            ans += min_cost[v]

            for u in range(V):
                min_cost[u] = min(min_cost[u], cost[v][u])

            print(f"v:{v}, used:{used}, min_cost:{min_cost}")

        return ans

    print(prim())

    return


if __name__ == '__main__':
    main()
