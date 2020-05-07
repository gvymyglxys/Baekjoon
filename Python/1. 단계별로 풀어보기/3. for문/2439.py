import sys

N = int(sys.stdin.readline().rstrip())

for n in range(1, N + 1): print('{}{}'.format(' ' * (N - n), '*' * n))