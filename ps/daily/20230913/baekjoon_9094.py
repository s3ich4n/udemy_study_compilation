import sys

size = input()
for _ in range(int(size)):
    print(" ".join([x[::-1] for x in sys.stdin.readline().split()]))
