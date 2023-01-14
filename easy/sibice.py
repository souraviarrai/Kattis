import math
loop,width,height = [int(i) for i in input().split()]
for i in range(loop):
    length = int(input())
    diagonal = math.sqrt((width **2) + (height **2))
    if length <= diagonal:
        print('DA')
    else:
        print('NE')
