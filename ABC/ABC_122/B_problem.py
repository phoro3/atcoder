S = input()

atgc = ['A', 'T', 'G', 'C']

max_count = 0
count = 0
for c in S:
    if c in atgc:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print(max_count)
