#! env python
# -*- coding: utf-8 -*-

import sys

# Ant-Book.main.py
# Date: 2021/12/30
# Filename: binary_tree.py
# Author: koucs

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
AtoZ = [chr(i) for i in range(65, 65 + 26)]
atoz = [chr(i) for i in range(97, 97 + 26)]
input = sys.stdin.readline


class Node:
    def __init__(self, v: int, lch: 'Node', rch: 'Node'):
        self.val = v
        self.lch, self.rch = lch, rch


def insert(p: Node, x: int) -> Node:
    if p is None:
        q = Node(x, None, None)
        return q
    else:
        if x < p.val:
            p.lch = insert(p.lch, x)
        else:
            p.rch = insert(p.rch, x)
        return p


def find(p: Node, x: int) -> bool:
    if p is None:
        return False
    elif x == p.val:
        return True
    elif x < p.val:
        return find(p.lch, x)
    else:
        return find(p.rch, x)


def remove(p: Node, x: int) -> Node:
    if p is None:
        return None
    elif x < p.val:
        p.lch = remove(p.lch, x)
    elif x > p.val:
        p.rch = remove(p.rch, x)
    elif p.lch is None:
        # Also, x == p.val
        # 削除したいノードが左の子を持っていない場合、右の子を持ってくる
        q = p.rch
        del p
        return q
    elif p.lch.rch is None:
        # Also, x == p.val AND p.lch is not None
        # 削除したいノード左の子が右の子を持っていない場合、左の子を持ってくる
        # (+ 削除したいノードの右の子を連結させる)
        q = p.lch
        q.rch = p.rch
        del p
        return q
    else:
        # Also, x == p.val AND p.lch is not None AND p.lch.rch is not None
        # どちらでもない (削除したいノードの左の子が右の子を持っている）場合
        # 左の子以下で最も大きいノードを削除したいノードの場所に持ってくる
        # (q は置き換わる最も大きい子に左の子がいる場合、それを親の右の子にする）
        q = p.lch
        while q.rch.rch is not None:
            q = q.rch
        r = q.rch
        q.rch = r.lch
        r.lch = p.lch
        r.rch = p.rch
        del p
        return r
    return p


def main():
    root = None
    root = insert(root, 1)
    print(find(root, 1))
    root = remove(root, 1)
    print(find(root, 1))

    root = insert(root, 5)
    root = insert(root, 10)
    print(find(root, 5))
    root = remove(root, 5)
    print(find(root, 5))
    return


if __name__ == '__main__':
    main()
