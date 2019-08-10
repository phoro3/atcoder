from collections import defaultdict
from math import factorial
N = int(input())
dic = defaultdict(int)

for i in range(N):
    sort_str = "".join(sorted(input()))
    dic[sort_str] += 1

count = 0
for key, val in dic.items():
    if val >= 2:
        count += factorial(val) // (factorial(2) * factorial(val - 2))
print(count)
