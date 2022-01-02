#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/01
# Filename: main.py 
# Author: koucs

import sys
sys.path.insert(0, '../../utils')
from kruskal import Edge, kruskal

INF = float('inf')


def main():
    N, M, R = map(int, input().split())
    edges = []
    for i in range(R):
        x, y, d = map(int, input().split())
        edges.append(Edge(x, M + y, -d))
    print(10_000 * (N + M) + kruskal(edges, N + M, R))
    return


if __name__ == '__main__':
    main()
