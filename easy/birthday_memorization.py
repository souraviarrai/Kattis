loop = int(input())
birthday_list = []
new_list = []
for i in range(loop):
    input_list = list(map(str,input().split()))[:3]
    birthday_list.append(input_list)

for i in range(len(birthday_list)):
    if birthday_list[i][2] not in new_list:
        new_list.append(birthday_list[i][0])
        
    
print(birthday_list)
print(new_list)

# my_list = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# new_list = []
# for i in range(len(my_list)):
#     new_list.append(my_list[i][2])
# print(new_list)
        
    
        

       
    
    
