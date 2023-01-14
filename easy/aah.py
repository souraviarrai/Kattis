list_input = []
for i in range(2):
    input_user = input()
    list_input.append(input_user)
if len(list_input[0]) >= len(list_input[1]):
    print('go')
else:
    print('no') 