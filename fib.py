import numpy as np
import copy
import sys
import time

def rec(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return rec(n-1) + rec(n-2)

def iterative(n):
    comped = [0, 1]
    if n < 2: return comped[n]
    for i in range(2, n):
        comped.append(comped[i-1]+comped[i-2])
    return comped[-1]

# requires numpy
def matrix(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else:
        fib = np.array([[0,1],[1,1]])
        temp = copy.deepcopy(fib)
        for i in range(2, n):
            temp = temp.dot(fib)
        base = np.array([[0],[1]])
        return temp.dot(base)[1][0]

def add_time(l, fun, n):
    t1 = time.time()
    fun(n)
    l.append(time.time() - t1)

def main():
    ts = []
    calls = [[rec,10],[rec,20],[rec,30],[rec,1],
             [iterative,10],[iterative,100],[iterative,1000],[iterative,10000],
             [matrix,10],[matrix,100],[matrix,1000],[matrix,10000]]
    for c in calls:
        add_time(ts,c[0],c[1])
    print("---------- |10          |100 (20 for rec)|1000 (30 for rec)|10000 (1 for rec)")
    print(f"recursive: {ts[0]}, {ts[1]}, {ts[2]}, {ts[3]}")
    print(f"iterative: {ts[4]}, {ts[5]}, {ts[6]}, {ts[7]}")
    print(f"matrix: {ts[8]}, {ts[9]}, {ts[10]}, {ts[11]}")


if __name__ == "__main__":
    main()