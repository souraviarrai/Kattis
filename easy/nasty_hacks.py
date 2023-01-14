loop = int(input())
for _ in range(loop):
    main_list = list(map(int,input().strip().split()))[:3]
    profit = main_list[1] - main_list[2]
    if (profit > main_list[0]):
        print('advertise')
    elif (profit == main_list[0]):
        print('does not matter')
    else:
        print('do not advertise')