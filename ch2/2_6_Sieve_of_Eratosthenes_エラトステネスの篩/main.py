#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/02
# Filename: main.py 
# Author: koucs
from typing import List, Tuple

MAX_N = 1_000_000


def sieve(n: int) -> Tuple[int, List[int]]:
    prime_list = []
    p = 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            prime_list.append(i)
            p += 1
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    return p, prime_list


def main():
    N = int(input())
    ans, prime_list = sieve(N)
    print(ans)
    return


if __name__ == '__main__':
    main()
