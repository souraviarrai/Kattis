x,y =[int(x) for x in input().split()]
if((0 < x and 0 < y ) and (x <= 1000000000 and x <= 1000000000)):
    if x < y:
        print(0)
    else:
        print(1)
