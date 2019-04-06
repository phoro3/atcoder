orders = [int(input()) for _ in range(5)]

rest = []
time = 0
for order in orders:
    if order % 10 == 0:
        time += order
    else:
        rest.append(order)

rest_mods = list(map(lambda x: x % 10, rest))

if len(rest_mods) > 0:
    min_mods_index = rest_mods.index(min(rest_mods))
    for i in range(len(rest)):
        time += rest[i]
        if i != min_mods_index:
            time += 10 - rest[i] % 10
else:
    time += sum(rest)
print(time)
