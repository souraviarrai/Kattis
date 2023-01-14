min_width = 2
min_height = 2
main_list = list(map(int,input().strip().split()))[:4]
width = main_list[0] - main_list[2]
height = main_list[1] - main_list[3]
if width >= min_width and height >= min_height:
    print('1')
else:
    print('0')
