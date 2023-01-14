string_list = [input() for _ in range(5)]

index_list = []
for i in range(len(string_list)):
    if 'FBI' in string_list[i]:
        index_list.append(i+1)

if index_list:
    print(*index_list)
else:
    print('HE GOT AWAY!')
