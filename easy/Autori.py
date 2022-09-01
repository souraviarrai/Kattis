fname = ''
name = [ i[0].upper() for i in input().split('-')]
for j in name:
    fname+=j
print(fname)