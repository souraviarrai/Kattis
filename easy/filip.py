x , y = map(str,input().split())
x_size , y_size =  len(x),len(y)
reversed_x , reversed_y = x[x_size::-1], y[y_size::-1]
if int(reversed_x) > int(reversed_y):
    print(reversed_x)
else:
    print(reversed_y)
