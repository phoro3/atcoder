N = int(input())
a_list = map(int, input().split())

total = 0
for a in a_list:
    total += 1 / a

print(1 / total)