city = []
count = []
for _ in range(eval(input())):
    for _ in range(eval(input())):
        name_of_city = input()
        if name_of_city not in city:
            city.append(name_of_city)
    count.append(len(city))
    city.clear()
for ele in count:
    print(ele)
