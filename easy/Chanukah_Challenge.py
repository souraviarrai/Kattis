cases = int(input())
for _ in range(cases):
    line = input().split()
    print(F"{line[0]} {int(int(line[1]) * (int(line[1])+1) / 2 + int(line[1]))}")