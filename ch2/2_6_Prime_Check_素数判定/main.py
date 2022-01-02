#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/02
# Filename: main.py 
# Author: koucs


def is_prime(n: int) -> bool:
    """
    自然数nが素数でない（合成数）ならば nは√n以下のいずれかの素数で割り切れる
    https://qr.paps.jp/8DvHU
    :param 自然数 n
    :return: bool
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n != 1


def main():
    n = int(input())
    ans = "Yes" if is_prime(n) else "No"
    print(ans)
    return


if __name__ == '__main__':
    main()
