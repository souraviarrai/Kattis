# interchanging first item and last item in a list



def swap(newlist):
    newlist[0],newlist[-1] = newlist[-1],newlist[0]
    return newlist

my_list = [1,2,3,4,5,6,9]
print(swap(my_list))