#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/02
# Filename: main.py 
# Author: koucs
# 格子点(lattice point) = 整数の点

def gcd(x: int, y: int):
    if y == 0:
        # gcd(x, 0) = x
        return x
    # Euclidean Algorithm
    return gcd(y, x % y)

def main():
    P1 = list(map(int, input().split()))
    P2 = list(map(int, input().split()))
    print(gcd(abs(P1[0] - P2[0]), abs(P1[1] - P2[1])) - 1)
    return


if __name__ == '__main__':
    main()
