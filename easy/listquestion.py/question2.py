# 12 .  Print a list after removing specified elements


# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# new_color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(new_color)


# squares = []
# for i in range(1,11):
#     item = i * i
#     squares.append(item)
# print(squares)

squares = [i*i for i in range(1,11)]
print(squares)
