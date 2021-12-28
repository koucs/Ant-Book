#! env python
# -*- coding: utf-8 -*-

import heapq
import sys

# Ant-Book.main.py
# Date: 2021/12/28
# Filename: main.py 
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    N, L, P = map(int, input().split())
    A = list(map(int, input().split()))  # Distance
    B = list(map(int, input().split()))  # Fuel

    # Set a Goal
    A += [L]
    B += [0]

    que = []
    ans, cur_pos, cur_tank = 0, 0, P

    for i in range(N + 1):
        print(f"{i}, {que}")
        next_distance = A[i] - cur_pos

        while (cur_tank - next_distance) < 0:
            if len(que) <= 0:
                print("-1")
                return
            ans += 1
            cur_tank += heapq.heappop(que) * -1

        cur_tank -= next_distance
        cur_pos = A[i]
        que.append(B[i] * -1)

    print(ans)
    return


if __name__ == '__main__':
    main()
