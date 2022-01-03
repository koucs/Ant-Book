#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/02
# Filename: main.py 
# Author: koucs
from typing import Tuple


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    ax + by = gcd(a, b) となる x,y を計算
    :param a:
    :param b:
    :return: gcd(a, b), x, y
    """
    print(f"a={a}, b={b}")
    d = a
    if b != 0:
        d, y, x = ext_gcd(b, a % b)
        print(f"ext_gcd(b, a % b): d={d}, y={y}, x={x}, a={a}, b={b}")
        y -= (a // b) * x
        # print(f"y -= (a // b) * x = {y}")
        print(f"a({a}) * x({x}) + b({b}) * y({y}) = d({d})")
    else:
        x, y = 1, 0
    return d, x, y


def main():
    a, b = map(int, input().split())
    d, x, y = ext_gcd(a, b)
    if d == 1:
        ans = [0, 0, 0, 0]
        if x > 0:
            ans[0] += x
        else:
            ans[1] += -x
        if y > 0:
            ans[2] += y
        else:
            ans[3] += -y
        print(*ans)
    else:
        print(-1)
    return


if __name__ == '__main__':
    main()
