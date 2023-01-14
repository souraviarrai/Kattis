import numpy as np
main_list = []
loop = int(input())
for _ in range(loop):
    city_list = []
    inner_loop = int(input())
    for _ in range(inner_loop):
        cities = input()
        city_list.append(cities)
        unique = len(np.unique(np.array(city_list)))
    main_list.append(unique)

for ele in main_list:
    print(ele)



