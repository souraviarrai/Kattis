order_list = []
user_input_no = list(map(int,input().split()))
user_input_alpha = input()
user_input_no.sort()
for ele in user_input_alpha:
    if ele == 'A':
        order_list.append(user_input_no[-3])
    if ele == 'B':
        order_list.append(user_input_no[-2])
    if ele == 'C':
        order_list.append(user_input_no[-1])
print(*order_list)
    


