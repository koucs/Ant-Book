#! env python
# -*- coding: utf-8 -*-

# Ant-Book.krusukal.py
# Date: 2022/01/02
# Filename: krusukal.py 
# Author: koucs

import operator
from typing import List

from union_find_tree import init, same, unite


class Edge:
    def __init__(self, u: int, v: int, cost: int):
        self.u, self.v, self.cost = u, v, cost

def kruskal(edges: List[Edge], V: int, E: int) -> int:
    edges.sort(key=operator.attrgetter("cost"))
    init(V)
    ans = 0
    for i in range(E):
        e = edges[i]
        if not same(e.u, e.v):
            unite(e.u, e.v)
            ans += e.cost
    return ans

