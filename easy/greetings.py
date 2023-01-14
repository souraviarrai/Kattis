greetings = input('')
message = greetings[0] + (greetings[1:-1]*2) + greetings[-1]
print(message)