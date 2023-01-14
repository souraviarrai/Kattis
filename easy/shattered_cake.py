width_of_cake = int(input())
pieces = int(input())
total_area = 0
for _ in range(pieces):
    width,height = [int(x) for x in input().split()]
    total_area += width * height
print(int(total_area / width_of_cake))