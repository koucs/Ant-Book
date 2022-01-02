#! env python
# -*- coding: utf-8 -*-

# Ant-Book.main.py
# Date: 2022/01/03
# Filename: main.py 
# Author: koucs
from typing import List

MAX_SEGMENT_LENGTH = 1_000_000  # b - a
MAX_SQRT_B = 1_000_000  # √b


def segment_sieve(a: int, b: int) -> List[int]:
    is_prime = [True] * (b - a)
    is_prime_small = [True] * MAX_SQRT_B

    i = 2
    while i * i < b:
        if is_prime_small[i]:
            # [2, √b) segment
            j = 2 * i
            while j * j < b:
                is_prime_small[j] = False
                j += i

            # [a, b) segment
            # a 以上の最小の i の倍数 を求める
            # https://algo-method.com/tasks/332/editorial
            # (別海)  j = (a + i - 1) // i * i
            j = a + (-a) % i
            if j == i:
                j *= 2
            while j < b:
                is_prime[j - a] = False
                j += i
        i += 1
    return is_prime


def main():
    a, b = map(int, input().split())
    is_prime = segment_sieve(a, b)
    print(sum(is_prime))
    return


if __name__ == '__main__':
    main()
