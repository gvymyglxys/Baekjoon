H, M = map(int, input().split())

if M >= 45: print(H, M - 45)
else: print((H - 1) % 24, M + 15)