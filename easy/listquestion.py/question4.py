# difference between two list 


list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
new_list = []
for i,j in zip(list1,list2):
    subtracted_item = i - j
    new_list.append(subtracted_item)
print(new_list)