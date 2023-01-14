test_case = int(input())
for i in range(test_case):
    input1 = input()
    input2 = input()
    list1,list2 = list(input1),list(input2)
    zipped = zip(list1,list2)
    new_list = []
    for ele1,ele2 in zipped:
        if ele1 == ele2:
            new_list.append('.')
        else:
            new_list.append('*')
    print(input1)
    print(input2)
    print(''.join(new_list))
    print()


