#! env python
# -*- coding: utf-8 -*-

# Ant-Book.prime.py
# Date: 2022/01/03
# Filename: prime.py
# Author: koucs


def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return i != 1
