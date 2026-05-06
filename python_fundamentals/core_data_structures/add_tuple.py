#!/usr/bin/env python3


def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 1:
        tuple_a1 = tuple_a[0]
    else:
        tuple_a1 = 0
    if len(tuple_a) >= 2:
        tuple_a2 = tuple_a[1]
    else:
        tuple_a2 = 0

    if len(tuple_b) >= 1:
        tuple_b1 = tuple_b[0]
    else:
        tuple_b1 = 0
    if len(tuple_b) >= 2:
        tuple_b2 = tuple_b[1]
    else:
        tuple_b2 = 0

    return (tuple_a1 + tuple_b1, tuple_a2 + tuple_b2)
