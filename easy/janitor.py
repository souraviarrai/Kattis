import math
sides = list(map(int,input().strip().split()))[:4]
semiperimeter = (sides[0]+ sides[1] + sides[2] + sides[3]) / 2
area = math.sqrt((semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]) * (semiperimeter - sides[3]))
print(area)