list3 = []
def mergelist(list1,list2):
    
    for ele in list1:
        list3.append(ele)
    for ele in list2:
        list3.append(ele)
    return list3
arr1 = [1,2,4]
arr2 = [1,3,4]

def mergesort(newest_list):
    if len(newest_list) > 1:
        left = newest_list[:len(newest_list)//2]
        right = newest_list[len(newest_list)//2:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                newest_list[k] = left[i]
                i+=1
            else:
                newest_list[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            newest_list[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            newest_list[k] = right[j]
            j+=1
            k+=1
    return newest_list

combined_list = mergelist(arr1,arr2)
ordered_list = mergesort(combined_list)
print(ordered_list)



    
        
