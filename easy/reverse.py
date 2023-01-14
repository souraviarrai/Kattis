my_list = []
loop = int(input())
for _ in range(loop):
    number = int(input())
    my_list.append(number)
my_list.reverse()
for ele in my_list:
    print(ele)