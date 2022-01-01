#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

INF = float('inf')
updated = False

def main():
    N, ML, MD = map(int, input().split())
    AL, BL, DL = [0] * ML, [0] * ML, [0] * ML
    for i in range(ML):
        AL[i], BL[i], DL[i] = map(int, input().split())
    AD, BD, DD = [0] * MD, [0] * MD, [0] * MD
    for i in range(MD):
        AD[i], BD[i], DD[i] = map(int, input().split())

    d = [0] * (N)

    def update(x: int, y: int, i: int):
        global updated
        if x > y:
            d[i] = y
            updated = True

    def bellmanford():
        for _ in range(N + 1):
            global updated
            updated = False

            # i+1 - (cost:0) -> i
            for i in range(0, N-1):
                print(f"i:{i}, d:{d}")
                if d[i + 1] < INF:
                    update(d[i], d[i + 1], i)
            # AL -> BL
            for i in range(ML):
                if d[AL[i] - 1] < INF:
                    update(d[BL[i] - 1], d[AL[i] - 1] + DL[i], BL[i] - 1)
            # AD -> BD
            for i in range(MD):
                if d[BD[i] - 1] < INF:
                    update(d[AD[i] - 1], d[DD[i] - 1] - DD[i], AD[i] - 1)

    bellmanford()

    global updated
    if updated:
        print("-1")
        return

    d = [INF] * N
    d[0] = 0

    bellmanford()

    ans = d[N-1]
    if ans == INF:
        ans = -1
    print(ans)

    return


if __name__ == '__main__':
    main()
