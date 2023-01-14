# Write a Python function that takes two lists and returns True if they have at least one common member.

lis1 = [1,2,3]
lis2 = [4,5,3]
def checker(list1,list2):
    for itemsx in list1:
        for itemsy in list2:
            if itemsx == itemsy:
                return True
    else:
        return False

if checker(lis1,lis2):
    print('YUP')
else:
    print('NOPE')

# list1 = [1,2,3]
# list2 = [4,5,3]      
# def commonMember(list1,list2):
#     result = False
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result

# if commonMember(list1,list2):
#     print('YES')
# else:
#     print('NO')
