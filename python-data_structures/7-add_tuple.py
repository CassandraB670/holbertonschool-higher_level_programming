#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        completeTupleA = tuple_a + (0,) * (2 - len(tuple_a))
        completeTupleB = tuple_b + (0,) * (2 - len(tuple_b))
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        completeTupleA = tuple_a[:2]
        completeTupleB = tuple_b[:2]
    else:
        completeTupleA = tuple_a
        completeTupleB = tuple_b
    res = []
    for index in range(0, len(tuple_a)):
        res.append(completeTupleA[index]+completeTupleB[index])
    res = tuple(res)
    return res
