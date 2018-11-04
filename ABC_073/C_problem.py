#coding:utf-8

N = int(input())
nums = set()

for i in range(N):
    A = int(input())

    if A in nums:
        nums.remove(A)
    else:
        nums.add(A)
print(len(nums))
