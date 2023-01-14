def mergesort(myarray):
    if len(myarray) > 1:

        left_myarray = myarray[:len(myarray)//2]
        right_myarray = myarray[len(myarray)//2:]

        mergesort(left_myarray)
        mergesort(right_myarray)

        i = j = k = 0

        while i < len(left_myarray) and j < len(right_myarray):
            if left_myarray[i] < right_myarray[j]:
                myarray[k] = left_myarray[i]
                i += 1
            else:
                myarray[k] = right_myarray[j]
                j += 1

            k+=1
        while i < len(left_myarray):
            myarray[k] = left_myarray[i]
            i += 1
            k += 1
        while j < len(right_myarray):
            myarray[k] = right_myarray[j]
            j += 1
            k += 1
array = [10,9,8,7,6,5,4,3,2,1]
mergesort(array)
print(array)
