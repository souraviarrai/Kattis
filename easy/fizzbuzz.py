x,y,z = map(int,input().split())
for i in range(1,z+1):
    divisible = False
    if i % x == 0:
        print('Fizz',end='')
        divisible = True
    if i % y == 0:
        print('Buzz',end='')
        divisible = True
    if not divisible:
        print(i,end='')
    print('')
    