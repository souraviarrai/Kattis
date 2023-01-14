# main_sum = 0
# main_list = []
# rows = int(input())

# for i in range(rows):
#     elements = list(map(int,input().split()))
#     main_list.append(elements)
   
# print(main_list)


no_of_elements = int(input())
main_list = list(map(int,input().strip().split()))[:no_of_elements]
main_sum = sum(main_list)
print(main_sum)