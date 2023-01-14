string = input()
small_str = string.lower()
vowels = ['a','e','i','o','u']
count = 0
for i in small_str:
    if i in vowels:
        count += 1
print(count)
    