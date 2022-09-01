a = int(input())
sum=0
for i in range(a):
    number = int(input())
    base = number//10
    power = number % 10
    sum += (base ** power)
print(sum)
    