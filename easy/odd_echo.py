loop = int(input())
listi = []
for i in range(loop):
    words = input()
    listi.append(words)
for index in range(len(listi)):
    if ((index+1) % 2 != 0):
        print(listi[index])
    

