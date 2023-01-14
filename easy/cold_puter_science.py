number_of_inputs = int(input())
list_of_temp = list(map(int,input().strip().split()))[:number_of_inputs]
count = 0
for i in range(len(list_of_temp)):
    if list_of_temp[i] < 0:
        count += 1
print(count)

