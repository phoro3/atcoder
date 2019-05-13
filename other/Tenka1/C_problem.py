N = int(input())
S = input()

white = len([char for char in S if char == '.'])

left_black = 0
right_white = white
result = left_black + right_white
for char in S:
    if char == '.':
        right_white -= 1
    else:
        left_black += 1
    result = min(result, right_white + left_black)
print(result)
