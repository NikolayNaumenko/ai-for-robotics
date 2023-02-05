from collections import deque

p = [0.2, 0.3, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2


def sense(pp, z):
    q = [pp[i] * (pHit if world[i] == z else pMiss) for i in range(len(pp))]
    q_sum = sum(q)

    return [el / q_sum for el in q]


def calc(pp, m, idx=0):
    if len(m) < idx + 1:
        return pp

    return calc(sense(pp, m[idx]), m, idx + 1)


def move(pp, u):
    # U = U % len(p)
    # q = p[-U:] + p[:-U]

    d = deque(pp)
    d.rotate(u)

    return d


print(move(p, 1))
