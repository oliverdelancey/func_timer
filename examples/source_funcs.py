#!usr/bin/env python
"""sample functions"""

def _utility1(a, b):
    return a * b

def alpha(x=3, y=_utility1(5, 6)):
    return 2 * x - y

def beta(a="s", b=3):
    a = a.lower()
    return len(a) + b
