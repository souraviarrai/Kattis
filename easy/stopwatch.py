number_of_presses = int(input())
is_running = False 
total_time = 0
previous_time = 0

for i in range(number_of_presses):
    current_time = int(input())
    if is_running:
        total_time += current_time - previous_time
    
    previous_time = current_time
    is_running = not is_running

if is_running:
    print('still running')
else:
    print(total_time)
