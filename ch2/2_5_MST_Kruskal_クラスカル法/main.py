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
    V = int(input())
    E = int(input())
    edges = []
    for _ in range(E):
        f, t, c = map(int, input().split())
        edges.append(Edge(f, t, c))

    print(kruskal(edges, V, E))
    return


if __name__ == '__main__':
    main()
