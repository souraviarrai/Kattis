Gcvwr,weightOfTruck,items = (input()).split()
items_weight = 0
item_list = list(int(num) for num in input().strip().split())[:int(items)]
for ele in range(0,len(item_list)):
    items_weight += item_list[ele]
difference_capacity = int(Gcvwr) - int(weightOfTruck)
capacity = difference_capacity * 0.9
trailer_weight = capacity - items_weight
print(int(trailer_weight))

