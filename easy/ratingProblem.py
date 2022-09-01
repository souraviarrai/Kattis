x,y = [int(x) for x in input().split()]
res = 0
for i in range(y):
    res += int(input())

sub = x - y
minimum = (res - 3*sub)/x
maximum = (res + 3*sub)/x
print(f'{minimum} {maximum}')


    

