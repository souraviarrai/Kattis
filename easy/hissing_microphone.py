# string = input()
# for i in range(len(string)):
#     if string[i] == 's':
#         if string[i+1] == 's':
#             print('hiss')
#             break
# else:
#     print('no hiss')

# string = input()
# if 'ss' in string:
#     print('hiss')
# else:
#     print('no hiss')
class Solution(object):
    def twoSum(nums, target):
        list_of_ans = []
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                list_of_ans.append(i)
                list_of_ans.append(i)
            return list_of_ans
                
    print(twoSum([2,7,11,15],9))