import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = [print(a, end = ' ') for a in sys.stdin.readline().rstrip().split() if int(a) < X]