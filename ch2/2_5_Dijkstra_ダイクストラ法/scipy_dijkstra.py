#! env python
# -*- coding: utf-8 -*-

import sys

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

# Ant-Book.main.py
# Date: 2021/12/31
# Filename: scipy_dijkstra.py
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


def main():
    graph = [
        [0, 2, 5, 0, 0, 0, 0],  # A
        [2, 0, 4, 6, 10, 0, 0], # B
        [5, 4, 0, 2, 0, 0, 0], # C
        [0, 6, 2, 0, 0, 1, 0], # D
        [0, 10, 0, 0, 0, 3, 5], # E
        [0, 0, 0, 1, 3, 0, 9], # F
        [0, 0, 0, 0, 5, 9, 0] # G
    ]
    graph = csr_matrix(graph)
    print(graph)
    dist_matrix, predecessors = dijkstra(csgraph=graph, directed=False, indices=0, return_predecessors=True)
    print(dist_matrix)
    print(predecessors)
    return


if __name__ == '__main__':
    main()
