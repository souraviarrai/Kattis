number = 7
number_as_a_list = list(int(num) for num in input().strip())
if number_as_a_list[0] == 5:
    if number_as_a_list[1] == 5:
        if number_as_a_list[2] == 5:
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    print(0)