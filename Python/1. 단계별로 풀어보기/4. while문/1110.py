import sys

N = int(sys.stdin.readline().rstrip())
A = N
B = 0
C = -1
cycle = 0

while C != N:

    cycle += 1
    B = ((A // 10) + (A % 10)) % 10
    C = ((A % 10) * 10) + B
    A = C

print(cycle)